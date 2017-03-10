#!/usr/bin/env python
# -*- coding: utf-8 -*-


from paramiko import *
import os
import subprocess


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

    # Método para lanzar ping
    @staticmethod
    def ping(host):
        with open(os.devnull, 'w') as DEVNULL:
            try:
                subprocess.check_call(
                    ['ping', '-c', '1', '-W', '1', '-i', '0.2', str(host)],
                    stdout=DEVNULL,  # suppress output
                    stderr=DEVNULL
                )
                is_up = True
            except subprocess.CalledProcessError:
                is_up = False
        return is_up

    # Método de creación de una conexión
    def connect(self, ssh, f0, username, password, key):
        try:
            ssh = SSHClient()
            ssh.set_missing_host_key_policy(AutoAddPolicy())
            ssh.connect(f0, username=username, password=password, timeout=10, pkey=key)
            return ssh
        except AuthenticationException:
            pass

    def get_ip(self, ip):
        return ip

    def get_codigo_centro(self, ssh):
        stdin, stdout, stderr = ssh.exec_command('cat /etc/puppet/data/info_centro | grep CODIGO=')
        print stderr
        codigo = stdout.read().split('CODIGO=')[1][0:-1]
        return codigo

    # E20 o TIC
    def get_tipo_centro(self, ssh):
        stdin, stdout, stderr = ssh.exec_command('cat /etc/puppet/data/info_centro | grep TIPO_CENTRO=')
        codigo = stdout.read().split('TIPO_CENTRO=')[1][0:-1]
        return codigo

    # Método de cierre de una conexión
    def close(self, ssh):
        ssh.close()