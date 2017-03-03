#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Dependencias:
# - python2.7
# - paramiko (pip install paramiko)
# - python-pexpect (pip install git+https://github.com/fgimian/paramiko-expect.git)


from Utils.server import *
from Utils.switch import *
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
    for i in lista_ips:
        s = Server(get_f0(i))
        ssh = s.connect(s.ssh, s.f0, s.username, s.password, s.key)
        for i in range(50, 40, -1):
            command = "fping -c1 -t500 192.168.4." + str(i) + " | awk '/loss/ {print $1}'"
            stdin, stdout, stderr = ssh.exec_command("fping -c1 -t500 192.168.4." + str(i) + " ")
            valor = stdout.read()
            if valor is not '':
                print "Ping a " + str(i) + bcolors.OKGREEN + " OK" + bcolors.ENDC
                tipo = Switch.get_tipo(s, ssh, "192.168.4." + str(i))
                print tipo
            else:
                print "Ping a " + str(i) + bcolors.FAIL + " KO" + bcolors.ENDC


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