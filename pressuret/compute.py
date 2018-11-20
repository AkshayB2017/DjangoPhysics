from numpy import exp, cos, linspace
import os, time, glob

def compute(n,t,v):
    """Return filename of plot of the damped_vibration function."""
    R=8.314
    p=R*float(n*t/v)
    return p
    # Use time since Jan 1, 1970 in filename in order make
    # a unique filename that the browser has not chached
    

if __name__ == '__main__':
    print (compute(1,1,1))