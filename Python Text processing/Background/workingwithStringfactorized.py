# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 16:30:30 2018

@author: DS-Tm
"""

#Factoring our code
#Our program here is now getting a little bit long, and a little bit complex. 
#There are lots of comments pointing out what specific sections do.
#Perhaps we can split it into functions to make it easier to read:


#A function to clean up (munge) a string to make it easy to match against
# (because we do the exact same thing to clean up names as we do to clean up the vote choice.)
#A function to check if someone has voted before
#A function to count a vote


#Have a try at breaking out some of the parts into functions, one function 
#at a time, without breaking the program.

#IPython Notebook makes this easy because you can run the cell 
#(with Shift-Enter if you like) after each change, to check the program still works

print("\n In the beginning \n")

#Create an empty dictionary for associating radish names with vote counts

counts = {}
#Create an empty list with the names of everyone who voted
voted = []
#Clean up (munge) a string so it's easy to match against other strings
def clean_string(s):
    return s.strip().capitalize().replace("  "," ")

#Check if someone has voted already and return True or False
def has_already_voted(name):
    if name in voted:
        print(name +"has already voted! fraud!")
        return True
    return False

#Count a vote for the radish variety named 'radish'
def count_vote(radish):
    if not radish in counts:
        #First vote for this variety
        counts[radish] = 1
    else:
        # Increment the radish count
        counts[radish] = counts[radish] + 1
        # counts[radish] + = 1

# starting with the file
for line in open ("radishsurvey.txt"):
    line = line.strip()
    name, vote = line.split(" - ")
    name = clean_string(name)
    vote = clean_string(vote)
    
    if not has_already_voted(name):
        count_vote(vote)
    voted.append(name)

print("Results: \n")
for name in counts:     
    print(name + ": " + str(counts[name]))
    
print("\n Finding the winner: First Option \n")

# Our program prints the number of votes cast for each radish variety,
# but it doesn't declare a winner. Can you update the program so it goes 
# through the votes counted and finds the one with the most votes?

# (You may want to add this as a totally separate cell, after the previous 
# cells, rather than modifying your existing loops.)

#You can make a for loop which iterates over all of the keys in a dictionary 
#by using the syntax for key in dictionary:. In this case it might be for name in counts:.

#from collections import OrderedDict
#maxs = 0
#aide = 0

for key, value in sorted(counts.items(), key=lambda item: (item[1], item[0])):
    print ("%s: %s" % (key, value))
    winner = key
    score  = value
#winner = counts.keys()[-1]
#els = list(counts.items())
#looser = els [0]
print("\n The winner is : " + winner + "\t with value of " + str(score) )
#print("\n The winner is : " + looser + "\t with value of ")
    
print("\n Finding the winner: Second Option \n")

# Record the winning name and the votes cast for it
winner_name = "No winner"
winner_votes = 0

for name in counts:
    if counts[name] > winner_votes:
        winner_votes = counts[name]
        winner_name = name

print("The winner is: " + winner_name + "\t with value of " + str(winner_votes))