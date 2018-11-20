from numpy import exp, cos, linspace
import os, time, glob

def compute(m,r):
    """Return filename of plot of the damped_vibration function."""
    G=6.67408*(10**-(11))
    g=-(G*m/(r**2))
    return g
    # Use time since Jan 1, 1970 in filename in order make
    # a unique filename that the browser has not chached
    

if __name__ == '__main__':
    print (compute(1,1))