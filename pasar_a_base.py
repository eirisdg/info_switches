#!/usr/bin/env python
# -*- coding: utf-8 -*-

fichero = 'big_lista'
fichero2 = 'big_lista_base'

archivo = open(fichero, 'r')
archivo2 = open(fichero2, 'w')
for line in archivo:
    ultimo = int(line.split('.')[-1]) - 2
    f0 = line.split('.')[0] + '.' + line.split('.')[1] + '.' + line.split('.')[2] + '.' + str(ultimo) + '\n'
    archivo2.write(f0)
archivo.close()
archivo2.close()