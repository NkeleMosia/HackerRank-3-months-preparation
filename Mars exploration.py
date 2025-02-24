#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    # Write your code here
    
    # Declare variables
    count = 0 
    s = s.upper()
    length = len(s)
    num_of_messages = 0
    
    
    # Iterate through the string - check for not "S" and "O"
    #for letter in s:
        
        # Checks for letters that are not "S" and "O"
        #if(letter != "S" and letter != "O"):
            #count += 1
            
    # Iterate through string - check order of letters
    
    for i in range(3, length, 3):
        
        if(s[i] != "S"):
            count += 1
        if(s[i + 1] != "O"):
            count += 1
        if(s[i - 1] != "S"):
            count  += 1
            
    # Check first 2 letters for "S" and "O"
    if(s[0] != "S"):
        count +=1
    if(s[1] != "O"):
        count += 1
        
    # Check iflast letter is "S"
    if(s[length - 1] != "S"):
        count += 1
    
    # Return number of letters changed
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
