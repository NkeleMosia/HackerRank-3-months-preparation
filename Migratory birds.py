#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    
    # Declare variables
    arr_set = set(arr) # Unique ids
    repeat = 0  # Will store occurances
    most_repeat_id = 0    # Will store id of most repeats
    repeat_most = 0   # Will store the most repeats recorded

    
    # Iterate through an array
    for bird_id_1 in arr_set:
        repeat = 0
        
        # Compare bid id 1 to bird id 2
        for bird_id_2 in arr:
            if(bird_id_1 == bird_id_2):
                repeat += 1
                
        # Check if repeat < most repeat found
        
        if(repeat > repeat_most):
            repeat_most = repeat
            most_repeat_id = bird_id_1
            
        # Picking the lessor id
            
        if(repeat == repeat_most) and (bird_id_1<most_repeat_id):
            most_repeat_id = bird_id_1
    
        
    
    # Check if id < id of most repeat
    
        # Set id of most repeat to current id
                      
        
    
    # Return the lowest id
    return most_repeat_id

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
