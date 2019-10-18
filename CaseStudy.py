# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 13:59:48 2019

@author: Carlotta

Title: Case Study
"""

import numpy as np 

np.random.seed(123) # initializes random numbers
random_walk = [0] # initializes the random_walk

for i in range(100) : # iterates 100 times
    step = random_walk[-1] #set step to the last elements of random_walk
    dice = np.random.randint(1,7) # rolls the dice

    if dice <= 2 :
        step -= 1
    elif dice <= 5 :
        step += 1
    else :
        step += np.random.randint(1,7)
        
    random_walk.append(step) # updates the last step


print(random_walk)
