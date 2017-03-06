#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Utils.switch import Switch

class Dell6224(Switch):

    def __init__(self, f0, ipsw):
        super(Dell6224,self).__init__(f0, ipsw)

    def get_ports_status(self):
        pass