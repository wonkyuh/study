#!/bin/bash

# 필요 패키지 설치
yum update -y && yum install -y net-tools iputils-ping vim procps yum-utils git wget expect

# 환경변수 설정
HOSTIP=$(ifconfig | grep -A 1 ens | tail -1 | awk '{print $2}')
HOSTIFACE=$(ifconfig | grep ens | cut -d ":" -f1)
master=192.168.88.10
node1=192.168.88.20
node2=192.168.88.30

# SELINUX 설정
sed -i 's/SELINUX=enforcing/SELINUX=disabled/g' /etc/sysconfig/selinux

# Hosts 수정
if [ $HOSTIP == $master ]; then
        hostnamectl set-hostname master
elif [ $HOSTIP == $node1 ]; then
        hostnamectl set-hostname node1
else
        [ $HOSTIP == $node2 ]
        hostnamectl set-hostname node2
fi

echo "$master master
$node1 node1
$node2 node2" >>/etc/hosts

# 컨테이너 내부 패킷 제어 설정
echo "
	net.bridge.bridge-nf-call-iptables = 1
	net.bridge.bridge-nf-call-ip6tables = 1
	net.ipv4.ip_forward = 1 " >>/etc/sysctl.conf

# SWAP 메모리 비활성화
sed -i '/ swap / s/^\(.*\)$/#\1/g' /etc/fstab
swapoff -a

# 도커 저장소 추가 및 설치
yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
yum -y install docker-ce-18.09.8 docker-ce-cli-18.09.8 containerd.io docker-compose-plugin

# 도커 데몬 실행
systemctl start docker
systemctl enable docker

# 도커 컴포즈 설치
curl -SL https://github.com/docker/compose/releases/download/v2.2.3/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose
ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
docker-compose version

# 도커 cgroup 드라이브 변경
touch /etc/docker/daemon.json
echo "{
    \"exec-opts\": [\"native.cgroupdriver=systemd\"]
}" >>/etc/docker/daemon.json
systemctl daemon-reload
systemctl restart docker

# 쿠버네티스 저장소 추가 및 설치
touch /etc/yum.repos.d/kubernetes.repo
echo "[kubernetes]
name=Kubernetes
baseurl=https://packages.cloud.google.com/yum/repos/kubernetes-el7-x86_64
enabled=1
gpgcheck=0
repo_gpgcheck=0
gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg
       https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg" >>/etc/yum.repos.d/kubernetes.repo
yum install -y kubelet-1.19.16-0.x86_64 kubectl-1.19.16-0.x86_64 kubeadm-1.19.16-0.x86_64

# 쿠버네티스 데몬 실행
systemctl enable kubelet
systemctl start kubelet

# 포트 방화벽 설정
firewall-cmd --permanent --add-port=80/tcp
firewall-cmd --permanent --add-port=443/tcp
firewall-cmd --permanent --add-port=2376/tcp
firewall-cmd --permanent --add-port=2379/tcp
firewall-cmd --permanent --add-port=2380/tcp
firewall-cmd --permanent --add-port=6443/tcp
firewall-cmd --permanent --add-port=8472/udp
firewall-cmd --permanent --add-port=9099/tcp
firewall-cmd --permanent --add-port=10250/tcp
firewall-cmd --permanent --add-port=10251/tcp
firewall-cmd --permanent --add-port=10252/tcp
firewall-cmd --permanent --add-port=10254/tcp
firewall-cmd --permanent --add-port=10255/tcp
firewall-cmd --permanent --add-port=30000-32767/tcp
firewall-cmd --permanent --add-port=30000-32767/udp
firewall-cmd --permanent --add-masquerade
firewall-cmd --reload

# 클러스터 구성을 위한 초기화 작업 수행
kubeadm init --apiserver-advertise-address=$HOSTIP --pod-network-cidr=10.244.0.0/16 >/root/K8sInitInfo

# kubeadm init 접속 정보 스크립트 생성
echo '#!/bin/bash' >/root/kubeadm.sh
cat /root/K8sInitInfo | tail -2 >>/root/kubeadm.sh

# kubectl 명령어 설정
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config

# kube-flannel 다운로드 및 네트워크 인터페이스 정보 추가
wget https://raw.githubusercontent.com/flannel-io/flannel/master/Documentation/kube-flannel.yml
sed -i'' -r -e "/--kube-subnet-mgr/a\        - --iface=$HOSTIFACE" ./kube-flannel.yml
kubectl apply -f kube-flannel.yml
systemctl restart kubelet
