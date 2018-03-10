# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 16:30:51 2018

@author: DS-Tm
"""

#How about if you just want to read a single line from a file?
#In Python, the control character for the end of a line is always represented as \n. 
#You can use \n in a string anywhere that you want to break a line:

#print("I want two lines!\nThe newline character gives me two lines.")
f = open("months.txt")
next = f.readline() #read() can also take an argument, which is the maximum number of characters to read from a file.
#Once read() has reached the end of the file, it returns an empty string (zero characters, the string "")
while next != "":
    print(next)
    next = f.readline()
    
#a = 'www.example.com'
#print(a.strip('mcowz.'))