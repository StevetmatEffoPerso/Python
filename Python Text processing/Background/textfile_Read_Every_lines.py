# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 17:28:04 2018

@author: DS-Tm
"""

#readline() will let you read through a file line by line. However, there are two even easier ways to read an entire file this way:
print("Read through a file line by line\n_________________________________")
f = open("months.txt")
print(f.readlines())
print()

print("You can then iterate over the list of lines like this:\n______________________________________________")
#The readlines() method reads all the lines in a file and returns them as a Python list.
#You can then iterate over the list of lines like this:
f = open("months.txt")
for month in f.readlines():
   print("Month " + month.strip())
print()

print("In fact, you don't even have to call readlines():\n")
print("Try to iterate through a text file with a for loop, It'll iterate through it line by line:\n______________________________________________")
f = open("months.txt")
for month in f:
   print("Month " + month.strip())