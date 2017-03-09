#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv


#server = ['10.181.106.64', 'TIC', '23700414', [['Dell-6224', '192.168.4.50', [u'1', u'1', 'Up'], [u'1', u'2', 'Down'], [u'1', u'3', 'Up'], [u'1', u'4', 'Down'], [u'1', u'5', 'Up'], [u'1', u'6', 'Up'], [u'1', u'7', 'Up'], [u'1', u'8', 'Up'], [u'1', u'9', 'Up'], [u'1', u'10', 'Up'], [u'1', u'11', 'Up'], [u'1', u'12', 'Up'], [u'1', u'13', 'Down'], [u'1', u'14', 'Down'], [u'1', u'15', 'Up'], [u'1', u'16', 'Up'], [u'1', u'17', 'Down'], [u'1', u'18', 'Down'], [u'1', u'19', 'Down'], [u'1', u'20', 'Down'], [u'1', u'21', 'Down'], [u'1', u'22', 'Down'], [u'1', u'23', 'Down'], [u'1', u'24', 'Down'], [u'1', u'g1', 'Down'], [u'1', u'g2', 'Down'], [u'1', u'g3', 'Down'], [u'1', u'g4', 'Down']]]]
#server = ['10.181.15.128', 'TIC', '23700499', [['DGS-1510-28', '192.168.4.50', [u'1', u'1', 'Up'], [u'1', u'2', 'Down'], [u'1', u'3', 'Up'], [u'1', u'4', 'Down'], [u'1', u'5', 'Up'], [u'1', u'6', 'Down'], [u'1', u'7', 'Up'], [u'1', u'8', 'Up'], [u'1', u'9', 'Up'], [u'1', u'10', 'Down'], [u'1', u'11', 'Up'], [u'1', u'12', 'Down'], [u'1', u'13', 'Up'], [u'1', u'14', 'Down'], [u'1', u'15', 'Down'], [u'1', u'16', 'Up'], [u'1', u'17', 'Up'], [u'1', u'18', 'Up'], [u'1', u'19', 'Down'], [u'1', u'20', 'Up'], [u'1', u'21', 'Down'], [u'1', u'22', 'Down'], [u'1', u'23', 'Up'], [u'1', u'24', 'Up'], [u'1', u'25', 'Down'], [u'1', u'26', 'Down']], ['DGS-1510-28', '192.168.4.50', [u'2', u'1', 'Down'], [u'2', u'2', 'Down'], [u'2', u'3', 'Down'], [u'2', u'4', 'Down'], [u'2', u'5', 'Down'], [u'2', u'6', 'Up'], [u'2', u'7', 'Up'], [u'2', u'8', 'Up'], [u'2', u'9', 'Up'], [u'2', u'10', 'Down'], [u'2', u'11', 'Down'], [u'2', u'12', 'Up'], [u'2', u'13', 'Down'], [u'2', u'14', 'Down'], [u'2', u'15', 'Down'], [u'2', u'16', 'Down'], [u'2', u'17', 'Up'], [u'2', u'18', 'Down'], [u'2', u'19', 'Down'], [u'2', u'20', 'Down'], [u'2', u'21', 'Down'], [u'2', u'22', 'Down'], [u'2', u'23', 'Down'], [u'2', u'24', 'Down'], [u'2', u'25', 'Down'], [u'2', u'26', 'Down']], ['DGS-1510-28', '192.168.4.50', [u'3', u'1', 'Down'], [u'3', u'2', 'Up'], [u'3', u'3', 'Up'], [u'3', u'4', 'Down'], [u'3', u'5', 'Down'], [u'3', u'6', 'Down'], [u'3', u'7', 'Down'], [u'3', u'8', 'Down'], [u'3', u'9', 'Down'], [u'3', u'10', 'Down'], [u'3', u'11', 'Up'], [u'3', u'12', 'Down'], [u'3', u'13', 'Down'], [u'3', u'14', 'Down'], [u'3', u'15', 'Up'], [u'3', u'16', 'Down'], [u'3', u'17', 'Down'], [u'3', u'18', 'Down'], [u'3', u'19', 'Up'], [u'3', u'20', 'Up'], [u'3', u'21', 'Down'], [u'3', u'22', 'Up'], [u'3', u'23', 'Down'], [u'3', u'24', 'Down'], [u'3', u'25', 'Down'], [u'3', u'26', 'Down']], ['DGS-1510-28', '192.168.4.50', [u'4', u'1', 'Down'], [u'4', u'2', 'Up'], [u'4', u'3', 'Down'], [u'4', u'4', 'Up'], [u'4', u'5', 'Down'], [u'4', u'6', 'Down'], [u'4', u'7', 'Up'], [u'4', u'8', 'Up'], [u'4', u'9', 'Down'], [u'4', u'10', 'Down'], [u'4', u'11', 'Down'], [u'4', u'12', 'Down'], [u'4', u'13', 'Down'], [u'4', u'14', 'Down'], [u'4', u'15', 'Down'], [u'4', u'16', 'Down'], [u'4', u'17', 'Down'], [u'4', u'18', 'Down'], [u'4', u'19', 'Up'], [u'4', u'20', 'Down'], [u'4', u'21', 'Down'], [u'4', u'22', 'Up'], [u'4', u'23', 'Down'], [u'4', u'24', 'Up'], [u'4', u'25', 'Down'], [u'4', u'26', 'Down']]], [['3com', '192.168.4.45']]]
server = ['10.181.73.224', 'TIC', '23700578', [['DGS-3427', '192.168.4.50', [1, u'1', 'Up'], [1, u'2', 'Up'], [1, u'3', 'Up'], [1, u'4', 'Up'], [1, u'5', 'Up'], [1, u'6', 'Up'], [1, u'7', 'Down'], [1, u'8', 'Down'], [1, u'9', 'Down'], [1, u'10', 'Down'], [1, u'11', 'Down'], [1, u'12', 'Down'], [1, u'13', 'Up'], [1, u'14', 'Down'], [1, u'15', 'Up'], [1, u'16', 'Down'], [1, u'17', 'Down'], [1, u'18', 'Down'], [1, u'19', 'Down'], [1, u'20', 'Down'], [1, u'21', 'Down'], [1, u'21F', 'Down'], [1, u'22', 'Down'], [1, u'22F', 'Down'], [1, u'23', 'Down'], [1, u'23F', 'Down'], [1, u'24', 'Down'], [1, u'24F', 'Down'], [1, u'25', 'Down'], [1, u'26', 'Down'], [1, u'27', 'Down']]]]


#lista = ['10.245.7.224', 'TIC','41002761',[['3com', '192.168.4.50'],['3com', '192.168.4.20']], [['3com', '192.168.4.49']], [['3com', '192.168.4.48']], [['3com', '192.168.4.47']]]


with open('server.csv', 'a') as csv1:
    writer = csv.writer(csv1, delimiter=';')
    contadorsw1 = 0
    contadorresto = 0
    marca = server[3][0][0]
    print marca
    for stack in server[3:]:
        tamanostack = len(stack)
        for switch in stack:
            if '3com' in switch or 'Allied Telesyn' in switch or 'Desconocido' in switch or tamanostack == 0:
                pass
            else:
                numpuertos = len(switch) - 2

                for i in range(0, numpuertos, +1):
                    if switch[i+2][2] == 'Down':
                        contadorresto += 1
                    if switch == server[3][0] and switch[i+2][2] == 'Down':
                        contadorsw1 += 1

    print contadorresto
    print contadorsw1

    writer.writerow([server[0], server[2]])
    writer.writerow([''])
    for stack in server[3:]:
        tamanostack = len(stack)
        for switch in stack:
            if '3com' in switch or 'Allied Telesyn' in switch or 'Desconocido' in switch or tamanostack == 0:
                writer.writerow(['SW', switch[0]])
                writer.writerow(['IP', switch[1]])
            else:
                puerto = []
                status = []
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
    writer.writerow('')


