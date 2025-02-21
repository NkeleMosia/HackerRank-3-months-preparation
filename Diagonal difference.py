#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    
    # Declare variacles
    size = len(arr)
    primary_arr = 0
    secondary_arr = 0
   
    
    
    # Write a loop
    for i in range(size):
        
        # find the sum of primary_arr and secondary_arr
        
        primary_arr += arr[i][i]
        secondary_arr += arr[i][(size - 1 - i)]
        
        # Find the difference b/n primary_arr an secondary_arr
        diag_difference = primary_arr - secondary_arr 
        
        
    
    # Return the absolute diagonal difference
    return abs(diag_difference)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
