from numpy import exp, cos, linspace
import os, time, glob
from math import sqrt

def compute(u,a,s):
    """Return filename of plot of the damped_vibration function."""
    v=sqrt((u*u)+(2*a*s))
    return v
    # Use time since Jan 1, 1970 in filename in order make
    # a unique filename that the browser has not chached
    

if __name__ == '__main__':
    print (compute(1, 1, 1))
