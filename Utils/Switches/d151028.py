#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Utils.switch import Switch
from paramiko import *
from paramiko_expect import *

class D151028(Switch):

    def __init__(self, f0, ipsw):
        super(D151028,self).__init__(f0, ipsw)

    # ([['DGS-1510-28']['X/xx', 'UP/DOWN'],['X/xx', 'UP/DOWN']],[['DGS-1510-28']['X/xx', 'UP/DOWN'],['X/xx', 'UP/DOWN']])
    def get_ports_status(self,ssh):
        stack = []
        switch = []
        try:
            sshtransport = ssh.get_transport()
            local_addr = (self.f0, 22)
            dest_addr = (self.ipsw, 22)
            sshchannel = sshtransport.open_channel("direct-tcpip", dest_addr, local_addr)

            sw = SSHClient()
            sw.set_missing_host_key_policy(AutoAddPolicy())
            sw.connect(self.f0, username='admin', password='ceycswtic', sock=sshchannel, timeout=5)

            interact = SSHClientInteraction(sw, timeout=1, display=False)
            interact.expect(['Switch#', 'Switch0#'])
            interact.send('show interface status')
            interact.send('a')
            interact.expect(['Switch#', 'Switch0#'])
            interact.send('logout')
            interact.close()
            sw.close()
            salida = interact.current_output_clean

            switch.append('DGS-1510-28')
            switch.append(str(self.ipsw))
            for line in salida.splitlines():
                if 'eth' in line:
                    unit = line.split('eth')[1][0]
                    boca = line.split('eth')[1][4:6]
                    if boca[1] == ' ':
                        boca = boca[0]
                    if 'not-connected' in line:
                        status = 'Down'
                    else:
                        status = 'Up'

                    if len(switch) > 1 and unit != switch[-1][0]:
                        stack.append(switch)
                        switch = []
                        switch.append('DGS-1510-28')
                        switch.append(str(self.ipsw))
                        switch.append([unit, boca, status])
                    else:
                        switch.append([unit, boca, status])
                elif 'Total Entries' in line:
                    stack.append(switch)
        except:
            stack = [['Error de conexión']]
        finally:
            return stack


    # Telnet
    def get_ports_status_tel(self,ssh):
        stack = []
        switch = []
        command = "telnet " + str(self.ipsw)
        try:
            stdin, stdout, stderr = ssh.exec_command(command, timeout=5)
            stdin.write('''admin\nceycswtic\nshow interfaces status\na\nq\nlogout\n''')
            outlines = stdout.readlines()
            salida = ''.join(outlines)
            switch.append('DGS-1510-28')
            switch.append(str(self.ipsw))
            for line in salida.splitlines():
                if 'eth' in line:
                    unit = line.split('eth')[1][0]
                    boca = line.split('eth')[1][4:6]
                    if boca[1] == ' ':
                        boca = boca[0]
                    if 'not-connected' in line:
                        status = 'Down'
                    else:
                        status = 'Up'

                    if len(switch) > 1 and unit != switch[-1][0]:
                        stack.append(switch)
                        switch = []
                        switch.append('DGS-1510-28')
                        switch.append(str(self.ipsw))
                        switch.append([unit, boca, status])
                    else:
                        switch.append([unit, boca, status])
                elif 'Total Entries' in line:
                    stack.append(switch)
        except:
            stack = [['Error de conexión']]
        finally:
            return stack