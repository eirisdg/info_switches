#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

from Utils.switch import Switch
from paramiko import *
from paramiko_expect import *

def get_salida(s, salida):
    return salida

class D3427(Switch):

    def __init__(self, f0, ipsw):
        super(D3427,self).__init__(f0, ipsw)

    def get_ports_status(self, ssh):
        sshtransport = ssh.get_transport()
        local_addr = (self.f0, 22)
        dest_addr = (self.ipsw, 22)
        sshchannel = sshtransport.open_channel("direct-tcpip", dest_addr, local_addr)

        sw = SSHClient()
        sw.set_missing_host_key_policy(AutoAddPolicy())
        sw.connect(self.f0, username='admin', password='ceycswtic', sock=sshchannel, timeout=5)

        salida = ''

        interact = SSHClientInteraction(sw, timeout=1, display=False)
        interact.send('\n')
        interact.expect(['DGS-3427:5#', 'DGS-3427:4#', 'DGS-3427:admin#'])
        modelo = interact.current_output

        if '1.20-B23' in modelo:
            interact.send('show ports\n')
            interact.send('n')
            interact.send('q')
            interact.send('\n')
            interact.expect(['DGS-3427:5#', 'DGS-3427:4#', 'DGS-3427:admin#'])
            salida = interact.current_output
            interact.send('\n')
            interact.send('logout')
        else:
            interact.send('show ports')
            interact.send('n')
            interact.send('q')
            interact.send('logout')
            interact.expect()
            salida = interact.current_output
        interact.close()
        sw.close()

        stack = []
        switch = []
        switch.append('DGS-3427')
        switch.append(str(self.ipsw))
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
        return stack