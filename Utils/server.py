#!/usr/bin/env python
# -*- coding: utf-8 -*-


from paramiko import *
import os
from paramiko_expect import *


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
            except AuthenticationException:
                print "No se ha podido conectar"
        return ssh


    def get_ip(self, ip):
        return ip

    def get_codigo_centro(self, ssh):
        stdin, stdout, stderr = ssh.exec_command('cat /etc/puppet/data/info_centro | grep CODIGO=')
        codigo = stdout.read().split('CODIGO=')[1][0:-1]
        return codigo

    def get_nombre_centro(self, ssh):
        stdin, stdout, stderr = ssh.exec_command('cat /etc/puppet/data/info_centro | grep NOMBRE=')
        nombre = stdout.read().split('NOMBRE=')[1][0:-1]
        return nombre

    # Método de cierre de una conexión
    def close(self, ssh):
        ssh.close()