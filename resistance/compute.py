from numpy import exp, cos, linspace
import os, time, glob

def compute(l,a):
    """Assume we are talking about resistivity of copper (1.72*10^-8)"""
    r=(1.72*(10**-8)*float(l/a))
    return r
    # Use time since Jan 1, 1970 in filename in order make
    # a unique filename that the browser has not chached
    

if __name__ == '__main__':
    print (compute(1,1))