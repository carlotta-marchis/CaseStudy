# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 13:59:48 2019

@author: Carlotta

Title: Case Study
"""

import numpy as np 
import matplotlib.pyplot as plt

np.random.seed(123) # initializes random numbers
all_walks = [] # initializes all_walks

for i in range(250) : # simulates random_walk 250 times
    random_walk = [0] # initializes the random_walk
    
    for i in range(100) : # iterates 100 times
        step = random_walk[-1] #set step to the last elements of random_walk
        dice = np.random.randint(1,7) # rolls the dice
    
        if dice <= 2 :
            step = max(0, step - 1) # this makes sure step doesn't go below 0
        elif dice <= 5 :
            step += 1
        else :
            step += np.random.randint(1,7)
            
        if np.random.rand() <= 0.001 : # implements clumsiness
            step = 0
            
        random_walk.append(step) # updates the last step

    all_walks.append(random_walk) # store the random_walk in all_walks

np_aw = np.array(all_walks)
plt.plot(np_aw)
plt.show()
plt.clf()

np_aw_t = np.transpose(np_aw)
plt.plot(np_aw_t)
plt.show()
plt.clf()

last_step = np_aw_t[-1,:] # select only the last step from each random_walk
plt.hist(last_step)
plt.show()

print(np.mean(last_step >= 60)) # This gives you the probability of reaching the 60th step after 100 dice rolls
# Note: last_step >= 60 generates an array of booleans, then you take the mean and obtain the probability you wanted
# print(last_step >= 60)
