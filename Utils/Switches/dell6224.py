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



        return resp