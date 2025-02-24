#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    
    # Declare variables
    highest = 0 # Highest point above sea
    lowest = 0  # Lowest point above sea
    sea_level = 0   # Level where we start drawing
    position = 0    # Used to find lowest and highest
    valleys = 0
    level = 0 # Used to count valleys
    
    # Decide on sea-level on grid
    
    for step in path:   # sea-level = highest - lowest
        if(step == 'U'):
            position +=1
        else:
            position -=1
        
        # Record highest and lowest position
        
        if(position > highest):
            highest = position
        if(position < lowest):
            lowest = position
            
    sea_level = highest - lowest 
    level = sea_level
        
    # Follow the path
    
    for step in path:   # sea-level = highest - lowest
        if(step == 'U'):
            level +=1
            if(level == sea_level):
                valleys+=1
        else:
            level -=1
            
        
    return valleys 
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
