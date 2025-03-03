#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    # Write your code here
    
    # Declare variables
    num_of_ways = 0    # Number of ways the chocolate can be divided
    contiguous_segment = 0 
    
    # Iterate through an array
    for i in range(len(s)):
        # Check integers that are equal to d and length is m
        contiguous_segment = s[i:i + m]
        if(sum(contiguous_segment) == d):
            num_of_ways += 1 #(contiguous_segment) # Adds the segments to the integers
            
    # Return number of ways
    return num_of_ways

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
