#Handy little functions
#Paul D. Simonson
#Updated 2021-03-26

import sys
import time
import os, errno  
#from os import listdir
#from os.path import isfile, join

def print_percent_done(i, total, increment = 100, sleep = 0):
    """
    My simple progess indicator.
    """
    if i % increment == 0 or i == total - 1:
        sys.stdout.write("\r" + str(round(100 * (i+1)/total,1)) + "% done")
        sys.stdout.flush()
        time.sleep(sleep)
        
def binomial(n, r):
    ''' Binomial coefficient, nCr, aka the "choose" function 
        n! / (r! * (n - r)!)
    '''
    p = 1    
    for i in range(1, min(r, n - r) + 1):
        p *= n
        p //= i
        n -= 1
    return p

def create_directory_if_necessary(directory_name = "../output/"):
    """Create an output folder, if it does not exist."""
    try:
        os.makedirs(directory_name)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
