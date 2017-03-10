#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Utils.switch import Switch
from paramiko import *
from paramiko_expect import *

class D121024(Switch):

    def __init__(self, f0, ipsw):
        super(D121024,self).__init__(f0, ipsw)

    def get_ports_status(self, ssh):
        stack = []
        try:
            sshtransport = ssh.get_transport()
            local_addr = (self.f0, 22)
            dest_addr = (self.ipsw, 22)
            sshchannel = sshtransport.open_channel("direct-tcpip", dest_addr, local_addr)

            sw = SSHClient()
            sw.set_missing_host_key_policy(AutoAddPolicy())
            sw.connect(self.f0, username='admin', password='ceycswtic', sock=sshchannel, timeout=5)

            interact = SSHClientInteraction(sw, timeout=1, display=False)
            interact.expect(['DGS-1210-24:admin#'])
            interact.send('debug info')
            interact.send('a')
            interact.expect(['DGS-1210-24:admin#'])
            interact.send('logout')
            interact.close()
            sw.close()
            salida = interact.current_output_clean

            switch1 = []
            switch1.append('DGS-1210-24')
            for line in salida.splitlines():
                if 'Learnt' in line:
                    unit = "1"
                    boca = line.split('Learnt')[1][6:8]
                    if boca[0] == ' ':
                        boca = boca[1]
                    else:
                        boca = boca[0:2]
                    status = 'Up'
                    switch1.append([unit, boca, status])
            switch2 = []
            switch2.append('DGS-1210-24')
            switch2.append(str(self.ipsw))
            for i in range(1, 29, +1):
                unit = 1
                boca = i
                if [str(unit), str(boca), 'Up'] in switch1:
                    switch2.append([unit, boca, 'Up'])
                else:
                    switch2.append([unit, boca, 'Down'])
            stack.append(switch2)
        except:
            stack = [['Error de conexión']]
        finally:
            return stack

    def get_ports_status_tel(self,ssh):
        command = "telnet " + str(self.ipsw)
        stack = []
        try:
            stdin, stdout, stderr = ssh.exec_command(command, timeout=5)
            contador = 0
            alldata = ""
            stdout.channel.settimeout(4)
            while not stdout.channel.exit_status_ready():
                solo_line = ""
                if stdout.channel.recv_ready():
                    solo_line = stdout.channel.recv(3048)
                    alldata += solo_line
                    if "UserName:" in solo_line:
                        stdin.channel.send('admin\n')
                    if "PassWord:" in solo_line:
                        stdin.channel.send('ceycswtic\n')
                    if "DGS-1210-24:admin#" in solo_line:
                        stdin.channel.send('debug info\n')
                        stdin.channel.send('a')
                        contador += 1
                    if contador is 2:
                        stdout.channel.close()

            salida = alldata
            switch1 = []
            switch1.append('DGS-1210-24')
            for line in salida.splitlines():
                if 'Learnt' in line:
                    unit = "1"
                    boca = line.split('Learnt')[1][6:8]
                    if boca[0] == ' ':
                        boca = boca[1]
                    else:
                        boca = boca[0:2]
                    status = 'Up'
                    switch1.append([unit, boca, status])
            switch2 = []
            switch2.append('DGS-1210-24')
            switch2.append(str(self.ipsw))
            for i in range(1, 29, +1):
                unit = 1
                boca = i
                if [str(unit), str(boca), 'Up'] in switch1:
                    switch2.append([unit, boca, 'Up'])
                else:
                    switch2.append([unit, boca, 'Down'])
            stack.append(switch2)
        except:
            stack = [['Error de conexión']]
        finally:
            return stack