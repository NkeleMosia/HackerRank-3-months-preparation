#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    
    # Declare variables
    final_grades = []   # Strores the final grades

    # Write the loop
    for grade in grades:
        
        #Checks if grade is less than 38
        if grade < 38:
            final_grades.append(grade)
            
        # If not < 38 and difference is less than 3
        else:
            next_mult_of_5 = (math.floor(grade / 5) + 1) * 5 
            difference = next_mult_of_5 - grade
            
            if difference < 3:
                final_grades.append(next_mult_of_5)
                
            # If not < 38 and difference is not less than 3
            else:
                final_grades.append(grade)
                
    return final_grades
            
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
