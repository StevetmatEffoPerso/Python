# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 13:35:19 2018

@author: DS-Tm
"""

foods = {}

foods["banana"] = "A delicious and tasty treat!"
foods["dirt"]   = "Not delicious. Not tasty. DO NOT EAT!"
foods["egg"]   = "Source of protein"
print(foods)
print("\n")

if "cheese" in foods:
    print("Cheese is one of the known foods!")
    print(foods["cheese"])
    
del foods["dirt"]
print("Foods without dirt\n")
print(foods)

ingredients = {}
ingredients["blt sandwich"] = ["bread", "lettuce", "tomato", "bacon"]
ingredients["egg"]   = "Source of protein"

print("\n")
print(ingredients)