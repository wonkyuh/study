#!/bin/bash/expect

# 대기시간
set timeout 30

# 명령어 입력
spawn ssh-keygen -t rsa

# 아래 문항 나올 시 입력
expect "Enter file in which to save the key (/root/.ssh/id_rsa):" {send "\n"}
expect "Enter passphrase (empty for no passphrase):" {send "\n"}
expect "Enter same passphrase again:" {send "\n"}

# 활성화
interact
