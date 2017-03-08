#!/usr/bin/env python
# -*- coding: utf-8 -*-
from paramiko import *
from paramiko_expect import *
import time

import time

from Utils.switch import Switch

f0 = '10.213.36.226'
username = 'root'
password = 'marajad3'
key = PKey('~/.ssh/id_dsa', password)

ssh = SSHClient()
ssh.set_missing_host_key_policy(AutoAddPolicy())
ssh.connect(f0, username=username, password=password, timeout=10, pkey=key)

command = "telnet 192.168.5.49"
stdin, stdout, stderr = ssh.exec_command(command, timeout=2)

contador = 0
alldata = ""
stdout.channel.settimeout(4)
while not stdout.channel.exit_status_ready():
    solo_line = ""
    if stdout.channel.recv_ready():
        solo_line = stdout.channel.recv(3048)
        alldata += solo_line
        if "User Name:" in solo_line:
            stdin.channel.send('admin\n')
        if "Password:" in solo_line:
            stdin.channel.send('ceycswtic\n')
        if "DGS-3100#" in solo_line:
            stdin.channel.send('show ports\n')
            stdin.channel.send('a')
            contador += 1
        if contador is 2:
            stdout.channel.close()


print alldata



stack = []
switch = []
switch.append('DGS-3100')
for line in alldata.splitlines():
            if 'Enabled' in line:
                unit = line[0]
                boca = line.split(':')[1][0:2]
                if boca[1] == ' ':
                    boca = boca[0]
                if 'Link Down' in line:
                    status = 'Down'
                    switch.append([unit, boca, 'Down'])
                else:
                    status = 'Up'
                    switch.append([unit, boca, 'Up'])

stack.append(switch)

print stack
