#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Write your code here
    
    # Declare variables
    from_front = 0      # Holds number of pages turned from the front
    from_back = 0       # Holds number of pages turned from the back
    
    # Check how many pages are flipped from the front
    from_front = p // 2
    
    # Check how many pages are flipped from the back
    from_back = (n // 2) - (p // 2)
    
    # Return minimum number of pages to turn
    return min(from_front, from_back)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
