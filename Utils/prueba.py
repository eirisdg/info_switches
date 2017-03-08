#!/usr/bin/env python
# -*- coding: utf-8 -*-

from paramiko import *

import time
from paramiko_expect import *

f0 = "10.181.101.34"
username = "root"
password = "marajad3"
key = PKey('~/.ssh/id_dsa', password)
ipsw = '192.168.4.50'

ssh = SSHClient()
ssh.set_missing_host_key_policy(AutoAddPolicy())
ssh.connect(f0, username=username, password=password, timeout=10, pkey=key)

command = "telnet " + str(ipsw)
stdin, stdout, stderr = ssh.exec_command(command)
stdin.write('''admin\nceycswtic\nshow interfaces status\na\nq\nlogout\n''')
outlines = stdout.readlines()
resp = ''.join(outlines)

stack = []
switch = []
switch.append('Dell-6224')
switch.append(str(ipsw))
for line in resp.splitlines():
    print line
    if 'Level' in line:
        unit = line[0]
        boca = line.split(unit + '/')[1][1:3]
        if boca[1] == ' ':
            boca = boca[0]
        if 'Up' in line:
            status = 'Up'
        else:
            status = 'Down'
        if len(switch) > 1 and unit != switch[-1][0]:
            stack.append(switch)
            switch = []
            switch.append('Dell-6224')
            switch.append(str(ipsw))
            switch.append([unit, boca, status])
        else:
            switch.append([unit, boca, status])
    elif 'console>logout' in line:
        stack.append(switch)

print stack