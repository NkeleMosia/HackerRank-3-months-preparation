#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    
    # Declare variables
    num_of_pairs = 0    # Stores the complete number of pairs which will be returned
    
    repeat = 0
    pairs = 0       # Stores the number of pairs for a single sock
    ar_set = set(ar) # Ar but with unique values
    
    # Iterate through an array 
    for sock_1 in ar_set:       # Pick a sock
        repeat = 0
        for sock_2 in ar:       # Compare with all the socks
            if(sock_1 == sock_2):
                repeat+=1
       
        pairs = int(repeat/2)   # Pairs of a single sock
        num_of_pairs+=pairs     # Add to complete number of pairs
        
        
    '''for color in counting_socks:
        if(color == 2):
            num_of_pairs +=1
        
    # Return number of matching pairs'''
    
    return num_of_pairs
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
