# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 13:35:19 2018

@author: DS-Tm
"""

shopping_list = []

shopping_list.append("milk")
shopping_list.append("cheese")
shopping_list.append("bread")

shopping_list2 = [ "diaper", "cheese", "beer", "SoftDrink" ]

print("First List")
print("\n ---------")
for item in shopping_list:
    print(item)
print("\n")

print("Second List")  
print("\n ---------")  
for item in shopping_list2:
    print(item)  

print("\n") 
shopping_list2.remove("cheese")
print("Second List after cheese removed") 
print("\n ------------------------------")
for item in shopping_list2:
    print(item)


print("\n -------------------------------")

if "milk" in shopping_list:
    print("Milk is Delicious!")

if "eggs" not in shopping_list:
    print("Well we can't have Eggs!")
    shopping_list.append("eggs")

print("\n") 
print("First List after Eggs added")
print("\n -----------------------------")
for item in shopping_list:
    print(item)