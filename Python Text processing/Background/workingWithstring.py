# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 17:56:33 2018

@author: DS-Tm
"""
from pprint import pprint
#as ridiculously contrived as this example is, I'm sure lots of you have come
# across situations where you have some data and you want to extract some relevant information from it

#From the previous chapter, we know that we can easily go through the file line by line,
# and each line will have a value like "Jin Li - White Icicle\n". We also know 
#that we can strip off the trailing newline with the strip() method:
list = []
for line in open("radishsurvey.txt"):
    line = line.strip()
    # Do something with each line
   # print(line)

#We need a way to split each line into the name and the vote. 
#Thankfully, Python comes with dozens of string methods including one called split().
# https://docs.python.org/3.3/library/stdtypes.html#str.split

    parts = line.split(" - ")
    #name, vote = parts
    name = parts[0]
    vote = parts[1]    
    #print(name + " voted for " + vote)

#There's a few things going on here, so let's go through it line by line. 
#Walking through a program in your head and thinking about 
#what each line does by itself is a good way to start to understand it
    
#a = "Jin Li - White Icicle".split("-")
#print(a)
    
#Can you write a program which only prints out the names of people who voted for White Icicle radishes?
#You'll need to compare the vote with the string "White Icicle", for each line in the file.
    if vote =="White Icicle":
        print(name + " likes White Icicle!")
        list.append(name)
print("\n")
        
#print("Counting votes for White Icicle...")
count = 0
for line in open("radishsurvey.txt"):
   line = line.strip()
   name, vote = line.split(" - ")
   if vote == "White Icicle":
      count = count + 1
print(count)
print("\n")
      
      
#print("\n")
#for a in list:
#   print(a)
#list.sort()     
#print("\n")
#for a in list:
#    print(a)

#Making a generic function
#a function definition where you specify an argument with the name of the radish you want to count votes for, 
#and the function returns the number of votes for that radish variety?
#

print("\n Making a generic function\n")
def count_votes(radish):
    print("Counting votes for " + radish + "...")
    count = 0
    for line in open("radishsurvey.txt"):
        line = line.strip()
        name, vote = line.split(" - ")
        if vote == radish:
            count = count + 1
    return count

print(count_votes("White Icicle"))

print(count_votes("Daikon"))

print(count_votes("Sicily Giant"))
print("\n")

#Counting All The Votes
#Counting votes for each radish variety is a bit time consuming,
#you have to know all the names in advance and you have to loop through the file multiple times.
#How about if you could automatically find all the varieties that were voted for,
#and count them all in one pass?
#You'll need a data structure where you can associate a radish variety with the
#number of votes counted for it. A dictionary would be perfect!
#Imagine a program that can count votes to create a dictionary with contents like this:

# Create an empty dictionary for associating radish names
# with vote counts

print("\n Counting All The Votes\n")
counts = {}

for line in open("radishsurvey.txt"):
    line = line.strip()
    name, vote = line.split(" - ")
    if vote not in counts:
        # First vote for this variety
        counts[vote] = 1
    else:
        # Increment the vote count
        counts[vote] = counts[vote] + 1
print(counts)

print("\n Pretty printing \n")

for name in counts:
    count = counts[name]
    print(name + ": " + str(count))

print("\n easy to pretty-print things. \n")
pprint(counts)

print("\n")
#Cleaning ("Munging") data
#Vote rigging! Probably not, it's just unclean data. To a computer, "Red King"
# and "red King" look different because of the different capitalisation. So do
# "Cherry Belle" and " Cherry Belle" because of the leading space.
#We need to clean up (sometimes called "munge") the data so it all looks the same.
#We already know one munging function, strip(). Try applying strip() to each voting choice,
#to remove distinctions like " Cherry Belle" and "Cherry Belle".
#How about "Red King" and "red king"? Take a look at the Python string functions reference 
#and see if you can find a function that could transform these two so they look 
#the same to the computer.
#https://docs.python.org/3/library/stdtypes.html#string-methods
#There are lots of functions which could remove the case distinction. str.lower()
#would convert all the names to all lower case, str.upper() would CONVERT THEM ALL TO UPPER CASE,
#or str.capitalize() would Capitalise the first letter only. Here's one way:
#

# Create an empty dictionary for associating radish names
# with vote counts

print("\n Cleaning Munging data\n")
counts = {}

for line in open("radishsurvey.txt"):
    line = line.strip()
    name, vote = line.split(" - ")
    # munge the vote string to clean it up
    vote = vote.strip().capitalize()
    if not vote in counts:
        # First vote for this variety
        counts[vote] = 1
    else:
        # Increment the vote count
        counts[vote] = counts[vote] + 1
pprint(counts)
#vote = vote.strip().capitalize() Which means "take the variable called vote, and call the strip()
#unction on it, and then call the capitalize() function on the result,
#and then assign that result back to the variable vote.
#This could be written in two lines like this, if you prefer:
#vote = vote.strip()
#vote = vote.capitalize()

print("\n There are still some funny votes counted in the output of this program: ")
print("\n Sicily  giant: 1 ")
print("\n Plum  purple: 1 ")
print("\n Cherry  belle: 1 ")
counts = {}

for line in open("radishsurvey.txt"):
    line = line.strip()
    name, vote = line.split(" - ")
    # munge the vote string to clean it up
    vote = vote.strip().capitalize()
    vote = vote.replace("  ", " ")
    if not vote in counts:
        # First vote for this variety
        counts[vote] = 1
    else:
        # Increment the vote count
        counts[vote] = counts[vote] + 1
pprint(counts)
#They all have something in common, a double space " " between the first and second words. Damn typos!
#strip() only cleaned up additional whitespace at the start and end of the string.
#The replace function can be used to replace all double spaces with a single space:
#vote = vote.replace("  ", " ")

print("\n Checking if anyone voted twice: First Option \n")

#You will need to start making a list of the names of everyone who has voted 
#so far. Each time you see a new name, check if it is already in the list of names.
# Starting with an empty list of names, you can use voterlist.append(newentry)
# to append a new entry to the end.
checks = {}
for line in open("radishsurvey.txt"):
    line = line.strip()
    name, vote = line.split(" - ")
    # munge both vote and name string
    vote = vote.strip().capitalize()
    vote = vote.replace("  ", " ")
    name = name.strip().capitalize()
    name = name.replace("  ", " ")
    if not name in checks:
        checks[name] = 1
    else:
        print(name + "\t duplicated \n")

print("\n Checking if anyone voted twice: Second Option \n")

# Create an empty dictionary for associating radish names
# with vote counts
counts = {}

# Create an empty list with the names of everyone who voted
voted = []

for line in open("radishsurvey.txt"):
    line = line.strip()
    name, vote = line.split(" - ")
    # clean up the person's name
    name = name.strip().capitalize().replace("  "," ")
    # check if this person already voted
    if name in voted:
        print(name + " has already voted! Fraud!")
        continue
    voted.append(name)
    # munge the vote string to clean it up
    vote = vote.strip().capitalize().replace("  "," ")
    if not vote in counts:
        # First vote for this variety
        counts[vote] = 1
    else:
        # Increment the vote count
        counts[vote] += 1

print("Results:")
print()
for name in counts:
    print(name + ": " + str(counts[name]))