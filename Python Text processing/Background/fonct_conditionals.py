# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 13:35:19 2018

@author: DS-Tm
"""

# -*- coding: utf-8 -*-

def addition(a, b):
    c = a + b
    print(c)

def soustraction(a, b):
    c = a - b
    print(c)
    
def division(a, b):
   
    if (a == 0 and b == 0):
        print("Indermination")
    if b == 0:
        print("Division par 0")
    else:              
        c = a/b
        print(c)

addition(5, 7)
soustraction(5, 7)
division(4, 0)
division(0, 0)
division(4, 9)


