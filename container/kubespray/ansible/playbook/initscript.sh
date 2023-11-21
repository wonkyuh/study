#!/bin/bash

# 환경변수 설정
HOSTIP=$(ifconfig | grep -A 1 ens | tail -1 | awk '{print $2}')
HOSTIFACE=$(ifconfig | grep ens | cut -d ":" -f1)
master=192.168.88.10
node1=192.168.88.20
node2=192.168.88.30

# Hosts 수정
if [ $HOSTIP == $master ]; then
        hostnamectl set-hostname master
elif [ $HOSTIP == $node1 ]; then
        hostnamectl set-hostname node1
else [ $HOSTIP == $node2 ]
        hostnamectl set-hostname node2
fi

# yum update
yum install -y epel-release
yum update -y

# SELINUX 설정
sed -i 's/SELINUX=enforcing/SELINUX=disabled/g' /etc/sysconfig/selinux

# SWAP 메모리 비활성화
sed -i '/ swap / s/^\(.*\)$/#\1/g' /etc/fstab
swapoff -a

# 공식 Docs에서 Local이면 firewalld 비활성화 권장
systemctl stop firewalld && systemctl disable firewalld

if [ $HOSTIP == $master ]; then
yum install -y ansible python3 libselinux-python3 git expect
echo "  net.bridge.bridge-nf-call-iptables = 1
	net.bridge.bridge-nf-call-ip6tables = 1
	net.ipv4.ip_forward = 1 " >>/etc/sysctl.conf

touch /root/symbolic.exp
cat << EOF > /root/symbolic.exp
#!/usr/bin/expect
set timeout 30
spawn rm /usr/bin/python
expect "rm: remove symbolic link ‘/usr/bin/python’?" {send "yes\n"}
interact 
EOF

chmod 755 /root/symbolic.exp
/root/symbolic.exp

ln -s /usr/bin/python3 /usr/bin/python
sed -i 's/python/python2/g' /usr/bin/yum
sed -i 's/python/python2/g' /usr/libexec/urlgrabber-ext-down

echo "	net.bridge.bridge-nf-call-iptables = 1
	net.bridge.bridge-nf-call-ip6tables = 1
	net.ipv4.ip_forward = 1 " >>/etc/sysctl.conf

git clone https://github.com/kubernetes-sigs/kubespray.git
cd kubespray
git checkout release-2.15
python3.6 -m pip install --upgrade pip
pip install -r /root/kubespray/requirements.txt

cp -rfp /root/kubespray/inventory/sample /root/kubespray/inventory/mycluster

cat << EOF > /root/kubespray/inventory/mycluster/inventory.ini
[all]
master        ansible_host=$master      ip=$master
node1         ansible_host=$node1       ip=$node1
node2         ansible_host=$node2       ip=$node2

[all:vars]
kubelet_cgroup_driver="systemd"

[kube-master]
master

[etcd]
master

[kube-node]
node1
node2

[calico-rr]

[k8s-cluster:children]
kube-master
kube-node
calico-rr
EOF

ansible-playbook -i /root/kubespray/inventory/mycluster/inventory.ini -e ansible_python_interpreter=/usr/bin/python2 -become --become-user=root /root/kubespray/cluster.yml

fi