#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv

lista = [['10.245.7.224', 'C.E.I.P. San Juan de Ribera', '41002761', '3com', '3com', '3com', '3com']]

colegio = "patata"
codigo = "patatita"



with open('prueba.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=';')
    spamwriter.writerow(["base:", colegio])
    spamwriter.writerow(["nombre:", codigo])
    spamwriter.writerow(["codigo:", codigo])
    spamwriter.writerow(["sw:", codigo])