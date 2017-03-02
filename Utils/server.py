#!/usr/bin/env python
# -*- coding: utf-8 -*-


from paramiko import *
import os


class Server:

    f0 = ""
    username = ""
    password = ""
    key = PKey('~/.ssh/id_dsa', password)
    ssh = None

    # Método constructor
    def __init__(self, f0):
        self.f0 = f0
        self.username = 'root'
        self.password = 'marajad3'


    # Método de creación de una conexión
    def connect(self, ssh, f0, username, password, key):
        ping = os.system("ping -c 1 " + f0 + " >/dev/null")
        if ping == 0:
            try:
                ssh = SSHClient()
                ssh.set_missing_host_key_policy(AutoAddPolicy())
                ssh.connect(f0, username=username, password=password, timeout=10, pkey=key)
                stdin, stdout, stderr = ssh.exec_command("pwd")
                print stdout.read().rstrip()
            except AuthenticationException:
                print "No se ha podido conectar"
        else:
            print "Servidor caído"
        return ssh


    # Método de cierre de una conexión
    def close(self, ssh):
        ssh.close()


    # Método para lanzar comando
    def command(self, ssh, command):
        stdin, stdout, stderr = ssh.exec_command(command)
        print stdout.read().rstrip()