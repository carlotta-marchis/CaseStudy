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

for i in range(10) : # simulates random_walk 10 times
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
            
        random_walk.append(step) # updates the last step

    all_walks.append(random_walk) # store the random_walk in all_walks

np_aw = np.array(all_walks)
plt.plot(np_aw)
plt.show()
plt.clf()

np_aw_t = np.transpose(np_aw)
plt.plot(np_aw_t)
plt.show()
