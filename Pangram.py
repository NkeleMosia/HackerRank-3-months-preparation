#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    
    # Declare variables
    size = 0
    letter_found = set()    # Keeps count of found letters
    s = s.lower()
    
    # Write a loop
    for letter in s:
        
        # Check if the string has all the letters
        if (re.match("[a-z]", letter)):
            letter_found.add(letter) # Stored found letters
    
    # Return if pangram or not pangram
    if(len(letter_found) == 26):   # If pangram
        return "pangram"
        
    else:   # If not pangram
        return "not pangram"
        
               
    
    
            
            
    
    
    # Return either pangram or not pangram
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
