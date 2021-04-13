# -*- coding: utf-8 -*-
# @Time    : 2021/4/12
# @Auther  : zhaoyuxiao
# @File    : SSHClientLocal.py
# @Software: PyCharm


import paramiko

# 创建SSH对象
ssh = paramiko.SSHClient()

# 把要连接的机器添加到known_hosts文件中
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 连接服务器
ssh.connect(hostname='192.168.106.130', port=22, username='root', password='xiaoyao45682')

# cmd = 'ps'
cmd = 'ls -l;ifconfig'       # 多个命令用;隔开
stdin, stdout, stderr = ssh.exec_command(cmd)

result = stdout.read()

if not result:
    result = stderr.read()
ssh.close()

print(result.decode())


