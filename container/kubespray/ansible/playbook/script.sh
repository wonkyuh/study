#!/bin/bash

# /etc/hosts 설정
echo "192.168.88.10 master
192.168.88.20 node1
192.168.88.30 node2" >>/etc/hosts

# SELINUX 설정
sed -i 's/SELINUX=enforcing/SELINUX=disabled/g' /etc/sysconfig/selinux

# 컨테이너 내부 패킷 제어 설정
echo "	net.bridge.bridge-nf-call-iptables = 1
	net.bridge.bridge-nf-call-ip6tables = 1
	net.ipv4.ip_forward = 1 " >>/etc/sysctl.conf

# SWAP 메모리 비활성화
sed -i '/ swap / s/^\(.*\)$/#\1/g' /etc/fstab
swapoff -a