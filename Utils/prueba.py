# -*- coding: utf-8 -*-

cadena = '''
show ports
Command: show ports

 Port      Port            Settings             Connection          Address
           State     Speed/Duplex/FlowCtrl  Speed/Duplex/FlowCtrl   Learning
 -------  --------  ---------------------  ----------------------  ---------
 1        Enabled   Auto/Disabled           1000M/Full/None         Enabled
 2        Enabled   Auto/Disabled           1000M/Full/None         Enabled
 3        Enabled   Auto/Disabled           1000M/Full/None         Enabled
 4        Enabled   Auto/Disabled           1000M/Full/None         Enabled
 5        Enabled   Auto/Disabled           1000M/Full/None         Enabled
 6        Enabled   Auto/Disabled           1000M/Full/None         Enabled
 7        Enabled   Auto/Disabled           Link Down               Enabled
 8        Enabled   Auto/Disabled           Link Down               Enabled
 9        Enabled   Auto/Disabled           Link Down               Enabled
 10       Enabled   Auto/Disabled           Link Down               Enabled
 11       Enabled   Auto/Disabled           Link Down               Enabled
 12       Enabled   Auto/Disabled           Link Down               Enabled
 13       Enabled   Auto/Disabled           Link Down               Enabled
 14       Enabled   Auto/Disabled           Link Down               Enabled
 15       Enabled   Auto/Disabled           Link Down               Enabled
 16       Enabled   Auto/Disabled           Link Down               Enabled
 17       Enabled   Auto/Disabled           1000M/Full/None         Enabled
 18       Enabled   Auto/Disabled           Link Down               Enabled
 19       Enabled   Auto/Disabled           1000M/Full/None         Enabled

CTRL+C ESC q Quit SPACE n Next Page p Previous Page r Refresh
 20       Enabled   Auto/Disabled           Link Down               Enabled
 21   (C) Enabled   Auto/Disabled           1000M/Full/None         Enabled
 21   (F) Enabled   Auto/Disabled           Link Down               Enabled
 22   (C) Enabled   Auto/Disabled           Link Down               Enabled
 22   (F) Enabled   Auto/Disabled           Link Down               Enabled
 23   (C) Enabled   Auto/Disabled           1000M/Full/None         Enabled
 23   (F) Enabled   Auto/Disabled           Link Down               Enabled
 24   (C) Enabled   Auto/Disabled           Link Down               Enabled
 24   (F) Enabled   Auto/Disabled           Link Down               Enabled
 25       Enabled   Auto/Disabled           Link Down               Enabled
 26       Enabled   Auto/Disabled           Link Down               Enabled
 27       Enabled   Auto/Disabled           Link Down               Enabled






Notes:(F)indicates fiber medium and (C)indicates copper medium in a combo port'''

for line in cadena.splitlines():
    if 'Enabled' in line or 'Auto/Disabled' in line:
        unit = 1
        boca = line[1:3]
        if 'Link Down' in line:
            status = 'Down'
        else:
            status = 'Up'

        print([unit, boca, status])
