# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 16:04:38 2018

@author: DS-Tm
"""

f = open("months.txt") #The open function creates a file object (a way of getting at the contents of the file), which is then stored in the variable f.
print(f.read()) #f.read() tells the file object to read the full contents of the file, and return it as a string.

print("\n")

#Reading by smaller pieces
f = open("months.txt")
next = f.read(1) #read() can also take an argument, which is the maximum number of characters to read from a file.
#Once read() has reached the end of the file, it returns an empty string (zero characters, the string "")
while next != "":
    print(next)
    next = f.read(1)