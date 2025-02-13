import math
import os
import random
import re
import sys

def timeConversion(s):
    
    # Declare variables
    #list_s = []
    #i = 0
    hh = 0
    mm = 0
    ss = 0
    m = ""
    present = ""    # This will be the string returned by the function
    
    # Slice s such that hh, mm and ss are assigned
    hh = s[0:2]     # Will return a string
    mm = s[3:5]
    ss = s[6:8]
    m = s[8:11]     # Storing if it is AM or PM 
    
    # Update hh to 24 hour value
    
    hh_int = int(hh)
    
    # Check for not 12 PM
    
    if m == "PM" and not hh == "12":
        hh_int += 12
        hh = str(hh_int)
        
    # Check for 12 AM
    
    if m == "AM" and hh == "12":
        hh = "00"
        
    # Check if hh is 24
    if hh == "24": 
        hh = "00"
        
    
    # Create the output string using present
    present = hh+":"+mm+":"+ss
    print(present)
    return present


if __name__ == '__main__':  # The main gate of the code
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    s = input()
    
    result = timeConversion(s)
    
    fptr.write(result + '\n')
    
    fptr.close()
    
    
