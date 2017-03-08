#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Utils.switch import Switch

class Dell6224(Switch):

    def __init__(self, f0, ipsw):
        super(Dell6224,self).__init__(f0, ipsw)

    def get_ports_status(self, ssh):
        command = "telnet " + str(self.ipsw)
        stdin, stdout, stderr = ssh.exec_command(command)
        stdin.write('''admin\nceycswtic\nshow interfaces status\na\nq\nlogout\n''')
        outlines = stdout.readlines()
        resp = ''.join(outlines)

        stack = []
        switch = []
        switch.append('Dell-6224', str(self.ipsw))

        for line in resp.splitlines():
            if 'Level' in line:
                unit = line[0]
                boca = line.split(unit + '/')[1][1:3]
                if 'Up' in line:
                    status = 'Up'
                else:
                    status = 'Down'

                if len(switch) > 1 and unit != switch[-1][0]:
                    stack.append(switch)
                    switch = []
                    switch.append('Dell-6224', str(self.ipsw))
                    switch.append([unit, boca, status])
                else:
                    switch.append([unit, boca, status])
            elif 'Flow Control:' in line:
                stack.append(switch)

        return stack