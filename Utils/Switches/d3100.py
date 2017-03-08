#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Utils.switch import Switch


class D3100(Switch):

    def __init__(self, f0, ipsw):
        super(D3100,self).__init__(f0, ipsw)

    def get_ports_status(self, ssh):
        command = "telnet " + str(self.ipsw)
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
        stack = []
        switch = ['DGS-3100']
        for line in alldata.splitlines():
            if 'Enabled' in line:
                unit = line[0]
                boca = line.split(':')[1][0:2]
                if boca[1] == ' ':
                    boca = boca[0]
                if 'Link Down' in line:
                    switch.append([unit, boca, 'Down'])
                else:
                    switch.append([unit, boca, 'Up'])
        stack.append(switch)