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
import csv

# Para observar el log de paramiko usar siempre Logger
logging.getLogger("paramiko").setLevel(logging.CRITICAL)
# Guarda en un fichero los resultados
util.log_to_file("paramiko.log")


fichero = "/tmp/pp"
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
    return ("========================\n"
            "===        MENU      ===\n"
            "========================\n"
            "\n"
            " 1. Configurar fichero\n"
            " 2. Escanear switches\n"
            "\n"
            " 0. Salir\n"
            "========================")

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
    if fichero != '':
        try:
            archivo = open(fichero, 'r')
            for line in archivo:
                lista_ips.append(line[0:-1])
            print "Lista de IPs cargada correctamente.\n"
        except IOError:
            print "No se puede abrir el archivo."
    else:
        print "No se ha introducido ningún fichero."


# Obtiene la IP de F0 de una ip base
def get_f0(ipbase):
    ultimo = int(ipbase.split('.')[-1]) + 2
    f0 = ipbase.split('.')[0] + '.' + ipbase.split('.')[1] + '.' + ipbase.split('.')[2] + '.' + str(ultimo)
    return f0

def save_to_csv_down(server):
    with open('server_down.csv', 'a') as csv1:
        writer = csv.writer(csv1, delimiter=';')
        writer.writerow([server])

def save_to_csv(server):
    with open('server.csv', 'a') as csv1:
        writer = csv.writer(csv1, delimiter=';')
        contadorsw1 = 0
        contadorresto = 0
        marca = server[3][0][0]
        if marca != 'Sin switches':
            for stack in server[3:]:
                tamanostack = len(stack)
                for switch in stack:
                    if '3com' in switch or 'Allied Telesyn' in switch or 'Desconocido' in switch or tamanostack == 0:
                        pass
                    else:
                        numpuertos = len(switch) - 2
                        for i in range(0, numpuertos, +1):
                            if switch[i + 2][2] == 'Down':
                                contadorresto += 1
                            if switch == server[3][0] and switch[i + 2][2] == 'Down':
                                contadorsw1 += 1

            writer.writerow([server[0],server[2], marca, contadorsw1, contadorresto - contadorsw1])
            for stack in server[3:]:
                tamanostack = len(stack)
                for switch in stack:
                    if '3com' in switch or 'Allied Telesyn' in switch or 'Desconocido' in switch or tamanostack == 0:
                        writer.writerow(['','','','','','SW', switch[0]])
                        writer.writerow(['','','','','','IP', switch[1]])
                    else:
                        puerto = ['','','','','']
                        status = ['','','','','']
                        puerto.append('SW')
                        puerto.append(switch[0])
                        status.append('IP')
                        status.append(switch[1])
                        numpuertos = len(switch) - 2
                        for i in range(0, numpuertos, +1):
                            puerto.append(switch[i + 2][1])
                            status.append(switch[i + 2][2])
                        writer.writerow(puerto)
                        writer.writerow(status)
            writer.writerow('')
            writer.writerow('')
        else:
            writer.writerow([server[0], server[2], marca])
            writer.writerow('')
            writer.writerow('')

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
                        #elif tipo == 'DGS-1210-24':
                        #     sw = D121024(s.f0, "192.168.4." + str(j))
                        #    ports = sw.get_ports_status(ssh)
                        elif tipo == 'DGS-3427':
                            sw = D3427(s.f0, "192.168.4." + str(j))
                            ports = sw.get_ports_status(ssh)
                        elif tipo == 'Dell-6224':
                            sw = Dell6224(s.f0, "192.168.4." + str(j))
                            ports = sw.get_ports_status(ssh)
                        elif tipo == 'DGS-1210-28':
                            sw = D121028(s.f0, "192.168.4." + str(j))
                            ports = sw.get_ports_status(ssh)
                        elif tipo == 'DGS-1210-24-Telnet':
                            sw = D121024(s.f0, "192.168.4." + str(j))
                            ports = sw.get_ports_status_tel(ssh)
                        elif tipo == 'DGS-3100':
                            sw = D3100(s.f0, "192.168.4." + str(j))
                            ports = sw.get_ports_status(ssh)
                        elif tipo == '3com':
                            ports = [['3com', '192.168.4.' + str(j)]]
                        elif tipo == 'Allied Telesyn':
                            ports = [['Allied Telesyn', '192.168.4.' + str(j)]]
                        elif tipo == 'Desconocido':
                            ports = [['Desconocido', '192.168.4.' + str(j)]]
                        else:
                            ports = [['Desconocido', '192.168.4.' + str(j)]]

                        stack.append(ports)
                    else:
                        print "Ping a 192.168.4." + str(j) + bcolors.FAIL + " KO" + bcolors.ENDC
                if len(stack) < 4:
                    stack.append([['Sin switches']])
                else:
                    servers.append(stack)
                save_to_csv(stack)
                print "Servidor " + ip + " guardado a CSV."
            except AuthenticationException as e:
                print("Fallo de conexión con el servidor " + str(i)) + ": \n" + e.message
                save_to_csv_down(i)
            except:
                print("Fallo de conexión con el servidor " + str(i)) + ": \n"
                save_to_csv_down(i)
        else:
            print "Servidor caído " + i
            servers.append([str(i), 'Sin conexión'])
            save_to_csv_down(i)


########### Aplicación principal ##################
if __name__ == "__main__":
    while True:
        print menu()
        opcion = input("Introduce una opción: ")

        if opcion == 1:
            configurar()

        elif opcion == 2:
            if fichero == "":
                print "No se ha establecido fichero de IPs"
            else:
                escanea()

        elif opcion == 0:
            print "Hasta luego!"
            break

        else:
            print "No has pulsado una función correcta"