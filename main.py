#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Función para imprimir menú
def menu():
    return ("====================\n"
            "===     MENU     ===\n"
            "====================\n"
            "\n"
            " 1. Configurar\n"
            " 2. \n"
            " 3. \n"
            " 4. \n"
            "\n"
            " 0. Salir\n"
            "====================")
def configurar():


while True:
    # Mostramos menú
    print menu()

    # Solicitamos la opción
    opcion = input("Introduce una opción: ")

    # Case para las opciones del menú
    if opcion == 1:
        configurar()

    elif opcion == 2:
        print opcion

    elif opcion == 3:
        print opcion

    elif opcion == 4:
        print opcion

    elif opcion == 0:
        print "Hasta luego!"
        break

    else:
        print "No has pulsado una función correcta"