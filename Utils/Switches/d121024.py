#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Utils.switch import Switch

class D121024(Switch):

    def __init__(self, f0, ipsw):
        super(D121024,self).__init__(f0, ipsw)

    def get_ports_status(self):
        pass