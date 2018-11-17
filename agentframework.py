# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 19:55:44 2018

@author: HP
"""

import random

class Agent():
    def __init__(self):
        self.x = random.randint(0,99)
        self.y = random.randint(0,99)

    def move(self):
        self.x = random.randint(0,99)
        self.y = random.randint(0,99)


