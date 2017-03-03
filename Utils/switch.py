#!/usr/bin/env python
# -*- coding: utf-8 -*-

from paramiko import *
from paramiko_expect import *

class Switch:

    @staticmethod
    def get_tipo(s,ssh, ipsw):
        tipo = ''
        if Switch.is_d1510(s,ssh,ipsw):
            tipo = 'DGS-1510-28'
        elif Switch.is_d121024(s, ssh, ipsw):
            tipo = 'DGS-1210-24'
        return tipo

    @staticmethod
    def is_d1510(s,ssh, ipsw):
        d1510 = None
        sshtransport = ssh.get_transport()
        local_addr = (s.f0, 22)
        dest_addr = (ipsw, 22)
        sshchannel = sshtransport.open_channel("direct-tcpip", dest_addr, local_addr)
        try:
            sw = SSHClient()
            sw.set_missing_host_key_policy(AutoAddPolicy())
            sw.connect(s.f0, username='admin', password='ceycswtic', sock=sshchannel, timeout=5)

            interact = SSHClientInteraction(sw, timeout=10, display=True)
            interact.expect('Switch#')
            interact.send('show unit 1')
            interact.expect('Switch#')
            modelo = interact.current_output_clean
            interact.close()
            sw.close()
            if 'DGS-1510-28' in modelo:
                d1510 = True
            else:
                d1510 = False
        except AuthenticationException:
            #print "No he podido conectar al Switch " + str(ipsw)
            d1510 = False
        finally:
            return d1510


    @staticmethod
    def is_d121024(s, ssh, ipsw):
        d121028 = None
        sshtransport = ssh.get_transport()
        local_addr = (s.f0, 22)
        dest_addr = (ipsw, 22)
        sshchannel = sshtransport.open_channel("direct-tcpip", dest_addr, local_addr)

        try:
            sw = SSHClient()
            sw.set_missing_host_key_policy(AutoAddPolicy())
            sw.connect(s.f0, username='admin', password='ceycswtic', sock=sshchannel, timeout=5)

            interact = SSHClientInteraction(sw, timeout=10, display=True)
            interact.expect('DGS-1210-24:admin#')

            modelo = interact.current_output_clean

            if 'DGS-1210-24' in modelo:
                d121028 = True
            else:
                d121028 = False
        except AuthenticationException:
            d121028 = False
        finally:
            return d121028

    #@staticmethod
    #def is_d121024():


    #@staticmethod
    #def is_d3427():

    #@staticmethod
    #def is_d3100():

