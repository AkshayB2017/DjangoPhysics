from numpy import exp, cos, linspace
import os, time, glob

def compute(n,t):
    """R=8.314"""
    u=1.5*8.314*float(n*t)
    return u
    # Use time since Jan 1, 1970 in filename in order make
    # a unique filename that the browser has not chached
    

if __name__ == '__main__':
    print (compute(1,1))