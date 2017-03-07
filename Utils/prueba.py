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
        print solo_line
        alldata += solo_line
        print solo_line
        if "User Name:" in solo_line:
            stdin.channel.send('admin\n')
        time.sleep(1)
        if "Password:" in solo_line:
            stdin.channel.send('ceycswtic\n')
        time.sleep(5)
        #stdin.channel.send('shows ports\n')
        if "DGS-3100#" in solo_line:
            stdin.channel.send('show ports\n')
            #time.sleep(1)
            stdin.channel.send('a')
            #stdin.channel.send('a')
            contador += 1
        if contador is 2:
            #stdin.channel.send('logout\n')
            stdout.channel.close()
time.sleep(3)
stdout.channel.close()

print alldata


for line in alldata.splitlines():
            if 'Enabled' in line:
                unit = line[0]
                unit = int(unit)
                #print unit
                boca = line.split(':')[1][0:2]
                print boca
                #unit += 1
                #boca = line.split('Learnt   Gi')[1][2:4]
                #if boca[1] == ' ':
                #    boca = boca[0]
                status = 'Up'



#for line in alldata.splitlines():
            #                if 'Enabled' in line:
            #           unit = line[0]
            #      #print unit
            #    boca = line.split(unit + '/')[1][1:3]
            #   if 'Full' in line:
            #      status = 'Up'
            #    else:
            #       status = 'Down'

            #     if len(switch) > 1 and unit != switch[-1][0]:
            #         stack.append(switch)
            #        switch = []
            #       switch.append('DGS-3100')
            #      switch.append([unit, boca, status])
            #    else:
            #        switch.append([unit, boca, status])
   # stack.append(alldata)
