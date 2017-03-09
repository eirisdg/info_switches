#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Dependencias:
# - python2.7
# - paramiko (pip install paramiko)
# - python-pexpect (pip install git+https://github.com/fgimian/paramiko-expect.git)

from Utils.server import *
from Utils.Switches.d151028 import *
from Utils.Switches.dell6224 import *
from Utils.Switches.d121024 import *
from Utils.Switches.d3427 import *
from Utils.Switches.d121028 import *
from Utils.Switches.d3100 import *

import logging

# Para observar el log de paramiko usar siempre Logger
logging.getLogger("paramiko").setLevel(logging.CRITICAL)
# Guarda en un fichero los resultados
util.log_to_file("paramiko.log")


fichero = "/home/eirisdg/PycharmProjects/info-switches/prueba"
lista_ips = []


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# Función para imprimir menú
def menu():
    return ("====================\n"
            "===     MENU     ===\n"
            "====================\n"
            "\n"
            " 1. Configurar\n"
            " 2. Escanear switches\n"
            " 3. \n"
            " 4. \n"
            "\n"
            " 0. Salir\n"
            "====================")

# Configura el fichero de ips
def configurar():
    global fichero
    fichero = raw_input("Introduce la ruta del fichero de IPs: ")
    try:
        archivo = open(fichero, 'r')
        archivo.close()
    except IOError:
        print "No se puede abrir el archivo."
        fichero = ""


# Carga la lista de IPs del fichero en el array
def carga_en_array():
    global fichero, lista_ips
    try:
        archivo = open(fichero, 'r')
        for line in archivo:
            lista_ips.append(line[0:-1])
        print "Lista de IPs cargada correctamente.\n"
    except IOError:
        print "No se puede abrir el archivo."


# Obtiene la IP de F0 de una ip base
def get_f0(ipbase):
    ultimo = int(ipbase.split('.')[-1]) + 2
    f0 = ipbase.split('.')[0] + '.' + ipbase.split('.')[1] + '.' + ipbase.split('.')[2] + '.' + str(ultimo)
    return f0


# Escanea la lista de ips de un archivo, las guarda en un array
def escanea():
    global lista_ips
    carga_en_array()
    servers = []
    for i in lista_ips:
        s = Server(get_f0(i))
        if Server.ping(s.f0):
            try:
                ssh = s.connect(s.ssh, s.f0, s.username, s.password, s.key)
                ip = s.get_ip(i)
                codigo_centro = s.get_codigo_centro(ssh)
                tipo = s.get_tipo_centro(ssh)
                print "\n\n===================================================\nConectado a centro " + codigo_centro + " con ip " + i + "\n==================================================="
                if tipo != 'E20':
                    stack = [ip, tipo, codigo_centro]
                    for j in range(50, 40, -1):
                        stdin, stdout, stderr = ssh.exec_command("fping -c1 -t100 192.168.4." + str(j) + " ")
                        valor = stdout.read()
                        if valor is not '':
                            print "Ping a 192.168.4." + str(j) + bcolors.OKGREEN + " OK" + bcolors.ENDC
                            tipo = Switch.get_tipo(s, ssh, "192.168.4." + str(j))
                            ports = ""
                            print tipo
                            if tipo == 'DGS-1510-28':
                                sw = D151028(s.f0, "192.168.4." + str(j))
                                ports = sw.get_ports_status(ssh)
                            elif tipo == 'DGS-1210-24':
                                sw = D121024(s.f0, "192.168.4." + str(j))
                                ports = sw.get_ports_status(ssh)
                            elif tipo == 'DGS-3427':
                                sw = D3427(s.f0, "192.168.4." + str(j))
                                ports = sw.get_ports_status(ssh)
                            elif tipo == 'Dell-6224':
                                sw = Dell6224(s.f0, "192.168.4." + str(j))
                                ports = sw.get_ports_status(ssh)
                            elif tipo == 'DGS-1210-28':
                                sw = D121028(s.f0, "192.168.4." + str(j))
                                ports = sw.get_ports_status(ssh)
                            elif tipo == 'DGS-3100':
                                sw = D3100(s.f0, "192.168.4." + str(j))
                                ports = sw.get_ports_status(ssh)
                            elif tipo == '3com':
                                ports = [['3com', '192.168.4.' + str(j)]]
                            elif tipo == 'Allied Telesyn':
                                ports = [['Allied Telesyn, 195.168.4.' + str(j)]]
                            else:
                                ports = 'unknown'

                            stack.append(ports)
                        else:
                            print "Ping a 192.168.4." + str(j) + bcolors.FAIL + " KO" + bcolors.ENDC
                    if len(stack) < 3:
                        stack.append('Sin switches')
                    else:
                        servers.append(stack)
                else:
                    stack = [ip, tipo, codigo_centro]
                print stack
            except AuthenticationException as e:
                print("Fallo de conexión con el servidor " + str(i)) + ": \n" + e.message
        else:
            print "Servidor caído " + i
            servers.append([str(i), 'Sin conexión'])
    print(servers)

# Aplicación principal
if __name__ == "__main__":
    while True:
        # Mostramos menú
        print menu()

        # Solicitamos la opción
        opcion = input("Introduce una opción: ")

        # Case para las opciones del menú
        if opcion == 1:
            configurar()

        elif opcion == 2:
            if fichero == "":
                print "No se ha establecido fichero de IPs"
                break
            else:
                escanea()

        elif opcion == 3:
            print opcion

        elif opcion == 4:
            print opcion

        elif opcion == 0:
            print "Hasta luego!"
            break

        else:
            print "No has pulsado una función correcta"