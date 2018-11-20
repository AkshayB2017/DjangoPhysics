from numpy import exp, cos, linspace
import os, time, glob
from math import sqrt

def compute(m,r):
    """Make constant of G as 6.67408*10^-11"""
    v=sqrt(2*6.67408*(10**-11)*m/r)
    return v
    # Use time since Jan 1, 1970 in filename in order make
    # a unique filename that the browser has not chached
    

if __name__ == '__main__':
    print (compute(1,1))