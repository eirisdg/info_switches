#!/usr/bin/env python
# -*- coding: utf-8 -*-

from paramiko import *
from paramiko_expect import *
import time

class Switch(object):
    f0 = ''
    ipsw = ''

    def __init__(self, f0, ipsw):
        self.f0 = f0
        self.ipsw = ipsw

    @staticmethod
    def get_tipo(s,ssh, ipsw):
        tipo = ''
        #nmap
        if Switch.is_3com(s,ssh,ipsw):
            tipo = '3com'
        elif Switch.is_at(s, ssh, ipsw):
            tipo = 'Allied Telesyn'
        #SSH
        elif Switch.is_d151028(s,ssh,ipsw):
            tipo = 'DGS-1510-28'
        elif Switch.is_d3427(s, ssh, ipsw):
            tipo = 'DGS-3427'
        # telnet
        elif Switch.is_121024_tel(s, ssh, ipsw):
            tipo = 'DGS-1210-24-Telnet'
        #ssh
        elif Switch.is_d121024(s, ssh, ipsw):
            tipo = 'DGS-1210-24'
        #telnet
        elif Switch.is_dell6224(s, ssh, ipsw):
            tipo = 'Dell-6224'
        elif Switch.is_d121028(s, ssh, ipsw):
            tipo = 'DGS-1210-28'
        elif Switch.is_d3100(s, ssh, ipsw):
            tipo = 'DGS-3100'
        else:
            tipo = "Desconocido"
        return tipo


    @staticmethod
    def is_3com(s, ssh, ipsw):
        com = None
        try:
            stdin, stdout, stderr = ssh.exec_command("nmap -sP -n " + ipsw)
            nmap = stdout.read()
            if '3Com' in nmap or '3com' in nmap:
                com = True
            else:
                com = False
            return com
        except:
            com = False
        finally:
            return com

    @staticmethod
    def is_at(s, ssh, ipsw):
        at = None
        try:
            stdin, stdout, stderr = ssh.exec_command("nmap -sP -n " + ipsw)
            nmap = stdout.read()
            if 'Allied Telesyn' in nmap:
                at = True
            else:
                at = False
        except:
            at = False
        finally:
            return at

    # SSH
    @staticmethod
    def is_d151028(s,ssh, ipsw):
        d1510 = None
        try:
            sshtransport = ssh.get_transport()
            local_addr = (s.f0, 22)
            dest_addr = (ipsw, 22)
            sshchannel = sshtransport.open_channel("direct-tcpip", dest_addr, local_addr)

            sw = SSHClient()
            sw.set_missing_host_key_policy(AutoAddPolicy())
            sw.connect(s.f0, username='admin', password='ceycswtic', sock=sshchannel, timeout=5)

            interact = SSHClientInteraction(sw, timeout=1, display=False)
            interact.expect(['Switch#','Switch0#'])
            interact.send('show unit 1')
            interact.expect(['Switch#','Switch0#'])
            interact.send('logout')
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

    # SSH
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

            interact = SSHClientInteraction(sw, timeout=1, display=False)
            interact.expect('DGS-1210-24:admin#')
            interact.send('logout')

            modelo = interact.current_output_clean
            interact.close()
            sw.close()

            if 'DGS-1210-24' in modelo:
                d121028 = True
            else:
                d121028 = False
        except Exception:
            d121028 = False
        finally:
            return d121028


    # SSH
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

            interact = SSHClientInteraction(sw, timeout=1, display=False)
            interact.expect(['DGS-3427:5#', 'DGS-3427:4#', 'DGS-3427:admin#'])
            modelo = interact.current_output_clean
            interact.send('logout')
            interact.expect()
            interact.close()
            sw.close()

            if 'DGS-3427' in modelo:
                d3427 = True
            else:
                d3427 = False
        except Exception:
            d3427 = False
        finally:
            return d3427


    # Telnet
    @staticmethod
    def is_121024_tel(s,ssh,ipsw):
        d121024 = None
        command = "telnet " + str(ipsw)
        try:
            stdin, stdout, stderr = ssh.exec_command(command, timeout=5)
            stdin.write('''admin\nceycswtic\nlogout\n''')
            outlines = stdout.readlines()
            resp = ''.join(outlines)
            if 'DGS-1210-24' in resp:
                d121024 = True
            else:
                d121024 = False
        except:
            d121024 = False
        finally:
            return d121024


    # Telnet
    @staticmethod
    def is_d121028(s, ssh, ipsw):
        d121028 = None
        command = "telnet " + str(ipsw)
        try:
            stdin, stdout, stderr = ssh.exec_command(command, timeout=5)
            stdin.write('''admin\nceycswtic\nlogout\n''')
            outlines = stdout.readlines()
            resp = ''.join(outlines)
            if 'DGS-1210-28' in resp:
                d121028 = True
            else:
                d121028 = False
        except:
            d121028 = False
        finally:
            return d121028


    # Telnet
    @staticmethod
    def is_d3100(s, ssh, ipsw):
        d3100 = None
        command = "telnet " + str(ipsw)
        try:
            stdin, stdout, stderr = ssh.exec_command(command, timeout=5)

            alldata = ""
            stdout.channel.settimeout(2)
            while not stdout.channel.exit_status_ready():
                solo_line = ""
                if stdout.channel.recv_ready():
                    solo_line = stdout.channel.recv(1024)
                    alldata += solo_line
                    print solo_line
                    if "User Name:" in solo_line:
                        stdin.channel.send('admin\n')

                    if "Password:" in solo_line:
                        stdin.channel.send('ceycswtic\n')

                    if "DGS-3100#" in solo_line:
                        stdin.channel.send('logout\n')
                time.sleep(3)
                stdout.channel.close()

            if 'DGS-3100' in alldata:
                d3100 = True
            else:
                d3100 = False
        except:
            d3100 = False
        finally:
            return d3100


    # Telnet
    @staticmethod
    def is_dell6224(s, ssh, ipsw):
        dell6224 = None
        command = "telnet " + str(ipsw)
        try:
            stdin, stdout, stderr = ssh.exec_command(command, timeout=5)
            stdin.write('''admin\nceycswtic\nshow system\nq\nlogout\n''')
            outlines = stdout.readlines()
            resp = ''.join(outlines)
            if 'PowerConnect 6224' in resp or 'Dell 24 Port' in resp:
                dell6224 = True
            else:
                dell6224 = False
        except:
            dell6224 = False
        finally:
            return dell6224

    def get_ports_status(self, ssh):
        pass