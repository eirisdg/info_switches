#!/usr/bin/env python
# -*- coding: utf-8 -*-

from paramiko import *
from paramiko_expect import *

class Switch:

    @staticmethod
    def get_tipo(s,ssh, ipsw):
        tipo = ''
        #nmap
        if Switch.is_3com(s,ssh,ipsw):
            tipo = '3com'
        #SSH
        elif Switch.is_d1510(s,ssh,ipsw):
            tipo = 'DGS-1510-28'
        elif Switch.is_d121024(s, ssh, ipsw):
            tipo = 'DGS-1210-24'
        elif Switch.is_d3427(s, ssh, ipsw):
            tipo = 'DGS-3427'
        #telnet
        elif Switch.is_d121028(s, ssh, ipsw):
            tipo = 'DGS-1210-28'
        return tipo


    @staticmethod
    def is_3com(s, ssh, ipsw):
        com = None
        stdin, stdout, stderr = ssh.exec_command("nmap -sP -n " + ipsw)
        nmap = stdout.read()
        if '3Com' in nmap:
            com = True
        else:
            com = False
        return com


    @staticmethod
    def is_d1510(s,ssh, ipsw):
        d1510 = None
        try:
            sshtransport = ssh.get_transport()
            local_addr = (s.f0, 22)
            dest_addr = (ipsw, 22)
            sshchannel = sshtransport.open_channel("direct-tcpip", dest_addr, local_addr)

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
        except Exception:
            d1510 = False
        finally:
            return d1510


    @staticmethod
    def is_d121024(s, ssh, ipsw):
        d121028 = None
        try:
            sshtransport = ssh.get_transport()
            local_addr = (s.f0, 22)
            dest_addr = (ipsw, 22)
            sshchannel = sshtransport.open_channel("direct-tcpip", dest_addr, local_addr)


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
        except Exception:
            d121028 = False
        finally:
            return d121028

    @staticmethod
    def is_d121028(s, ssh, ipsw):
        d121028 = None
        command = "telnet " + str(ipsw)
        stdin, stdout, stderr = ssh.exec_command(command)

        stdin.write('''admin\nceycswtic\nlogout\n''')

        outlines = stdout.readlines()
        resp = ''.join(outlines)
        if 'DGS-1210-28' in resp:
            d121028 = True
        else:
            d121028 = False
        return d121028

    @staticmethod
    def is_d3427(s, ssh, ipsw):
        d3427 = None
        try:
            sshtransport = ssh.get_transport()
            local_addr = (s.f0, 22)
            dest_addr = (ipsw, 22)
            sshchannel = sshtransport.open_channel("direct-tcpip", dest_addr, local_addr)

            sw = SSHClient()
            sw.set_missing_host_key_policy(AutoAddPolicy())
            sw.connect(s.f0, username='admin', password='ceycswtic', sock=sshchannel, timeout=5)

            interact = SSHClientInteraction(sw, timeout=10, display=True)
            interact.expect('DGS-3427:4#')

            modelo = interact.current_output_clean

            if 'DGS-3427' in modelo:
                d3427 = True
            else:
                d3427 = False
        except Exception:
            d121028 = False
        finally:
            return d3427

    #@staticmethod
    #def is_d3100():

