#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Utils.switch import Switch
from paramiko import *
from paramiko_expect import *

class D151028(Switch):

    def __init__(self, f0, ipsw):
        super(D151028,self).__init__(f0, ipsw)

    # (['X/xx', 'UP/DOWN'],['X/xx', 'UP/DOWN'],['X/xx', 'UP/DOWN'],['X/xx', 'UP/DOWN'])
    def get_ports_status(self,ssh):
        sshtransport = ssh.get_transport()
        local_addr = (self.f0, 22)
        dest_addr = (self.ipsw, 22)
        sshchannel = sshtransport.open_channel("direct-tcpip", dest_addr, local_addr)

        sw = SSHClient()
        sw.set_missing_host_key_policy(AutoAddPolicy())
        sw.connect(self.f0, username='admin', password='ceycswtic', sock=sshchannel, timeout=5)

        interact = SSHClientInteraction(sw, timeout=1, display=True)
        interact.expect(['Switches#', 'Switch0#'])
        interact.send('show interface status')
        interact.send('a')
        interact.expect(['Switches#', 'Switch0#'])
        interact.send('logout')
        puertos = interact.current_output_clean



        return(puertos)
