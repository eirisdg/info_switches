#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

from Utils.switch import Switch
from paramiko import *
from paramiko_expect import *

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

        interact = SSHClientInteraction(sw, timeout=1, display=False)
        interact.expect(['DGS-3427:5#', 'DGS-3427:4#'])
        interact.send('show ports\n')
        interact.send('n')
        interact.send('n')
        interact.send('n')
        interact.send('n')
        interact.send('n')
        interact.send('n')
        interact.send('n')
        interact.send('q')
        salida = interact.current_output_clean
        print salida
        interact.expect(['DGS-3427:5#', 'DGS-3427:4#'])
        interact.send('logout\n')
        interact.expect()
        #salida = interact.current_output_clean
        interact.close()
        sw.close()

        stack = []
        switch = []

        for line in salida.splitlines():
            pass

        return salida