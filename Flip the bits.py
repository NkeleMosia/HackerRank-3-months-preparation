#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    # Write your code here
    
    # Declare variables
    pos_dec_int = 0     # Will store the returned sum of the flipped bits
    unflipped_bits_list = []      # Will store the list of bits
    multiples_list = []     # Will store the list of multiples
    flipped_bits_list = [0]*32 # Will store the flipped list
    
    
    
    
    # Turn the number into 32 bits
    
    # Create 2^i from 2^31 to 2^0
    
    for i in range(31,-1,- 1):
        
        # Check if divisible by 2^i
        
        div = 2**i   # Makes code neat
        
        if(n/div >= 1 ):
            unflipped_bits_list.append(1) # Set 2^i bit to 1
            n-=div  # minus 2^i from n
        else:
            unflipped_bits_list.append(0) # Set 2^i bit to 0
            
    # Time to flip
    
    # Iterate through array
    
    for j in range (32):
        if(unflipped_bits_list[j] == 1):    # Check if bit it 1
            flipped_bits_list[j] = 0    # Flip
        else:
            flipped_bits_list[j] = 1    # Flip
            
    # Convert to flipped bits to decimal
    
    for k in range (32):    # List index
        power = 31 - k # To create decimal value with
        if(flipped_bits_list[k] == 1):
            pos_dec_int += 2**power # Add decimal value to final return value
            
    return pos_dec_int
            
    
    # Combine the 2 lists into key pair value list
    
    # Find the positive decimal integer
    
    # Return the positive decimal integer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
