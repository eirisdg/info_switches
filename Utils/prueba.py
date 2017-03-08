#!/usr/bin/env python
# -*- coding: utf-8 -*-

from paramiko import *
from paramiko_expect import *

f0 = "10.117.57.226"
username = "root"
password = "marajad3"
key = PKey('~/.ssh/id_dsa', password)
ipsw = '192.168.4.50'

ssh = SSHClient()
ssh.set_missing_host_key_policy(AutoAddPolicy())
ssh.connect(f0, username=username, password=password, timeout=10, pkey=key)

sshtransport = ssh.get_transport()
local_addr = (f0, 22)
dest_addr = (ipsw, 22)
sshchannel = sshtransport.open_channel("direct-tcpip", dest_addr, local_addr)

sw = SSHClient()
sw.set_missing_host_key_policy(AutoAddPolicy())
sw.connect(f0, username='admin', password='ceycswtic', sock=sshchannel, timeout=4)

interact = SSHClientInteraction(sw, timeout=1, display=False)
interact.expect(['DGS-3427:5#', 'DGS-3427:4#'])
interact.send('show ports')
interact.send('n')
interact.send('q')
interact.send('logout')
interact.expect()
salida = interact.current_output
interact.close()
sw.close()
ssh.close()

stack = []
switch = []
switch.append('DGS-3427')
switch.append(str(ipsw))
for line in salida.splitlines():
    if 'Enabled' in line or 'Auto/Disabled' in line:
        unit = 1
        boca = line[1:3]
        if boca[1] == ' ':
            boca = boca[0]
        if '(F)' in line:
            boca += 'F'
        if 'Link Down' in line:
            status = 'Down'
        else:
            status = 'Up'
        switch.append([unit, boca, status])

    if 'Notes:(F)indicates' in line:
        stack.append(switch)

print stack