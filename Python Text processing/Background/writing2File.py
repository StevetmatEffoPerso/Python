# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 17:37:24 2018

@author: DS-Tm
"""

#When you open() a file, you can optionally specify a file mode, which tells Python what you want to do with
#the file. The default mode is r for read, but another mode is w to write to a file.
#Tip: the write (w) mode will write completely new contents to a file, wiping out what it had previously!
#other types:https://docs.python.org/3/library/functions.html#open

f = open("awesomenewfile.txt", "w")
f.write("Awesome message!")
f.close()
l = open ("awesomenewfile.txt", "r")
print(l.readlines())

#Can you write a program which creates a two line text file?

print("\n Creates a two line text file\n")
k = open("mylongfile.txt", "w")
k.write("First line\n")
k.write("Second line")
k.close()
p = open ("mylongfile.txt", "r")
print(p.readlines())