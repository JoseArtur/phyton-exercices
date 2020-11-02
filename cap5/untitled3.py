# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 10:11:59 2020

@author: josea
"""

import random
import turtle
def is_in_screen(w,t):
    if random.random()>0.1:
        return True
    else:
        return False
wn=turtle.Screen()
wn.setup(500,600)
wn.bgcolor("green")
tess=turtle.Turtle()
tess.shape("turtle")
~while is_in_screen(wn,tess):
    coin=random.randrange(0,2)
    if