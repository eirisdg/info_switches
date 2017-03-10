#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Utils.switch import Switch

class D121028(Switch):

    def __init__(self, f0, ipsw):
        super(D121028,self).__init__(f0, ipsw)

    def get_ports_status(self, ssh):
        stack = []
        switch1 = []
        try:
            command = "telnet " + str(self.ipsw)
            stdin, stdout, stderr = ssh.exec_command(command, timeout=5)
            stdin.write('''admin\nceycswtic\ndebug info\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nlogout\n''')
            outlines = stdout.readlines()
            resp = ''.join(outlines)

            switch1.append('DGS-1210-28')
            unitmax = int(0)
            for line in resp.splitlines():
                if 'Learnt' in line:
                    unit = line.split('Learnt   Gi')[1][0]
                    unit = int(unit)
                    unit += 1
                    boca = line.split('Learnt   Gi')[1][2:4]
                    if boca[1] == ' ':
                        boca = boca[0]
                    status = 'Up'
                    if unit > unitmax:
                        unitmax = unit

                    switch1.append([unit, boca, status])

            switch2 = []
            switch2.append('DGS-1210-28')
            switch2.append(str(self.ipsw))
            for a in range(0, unitmax, +1):
                for i in range(1, 29, +1):
                    unit = 1
                    boca = i
                    if [unit, str(boca), 'Up'] in switch1:
                        switch2.append([unit, boca, 'Up'])
                    else:
                        switch2.append([unit, boca, 'Down'])
                stack.append(switch2)
        except:
            stack = [['Error de conexión']]
        finally:
            return stack