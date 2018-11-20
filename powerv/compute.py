from numpy import exp, cos, linspace
import os, time, glob

def compute(a,t,d):
    """lET k be value of air at 25 degree celsius """
    k=0.0262
    p=k*float(a*t/d)
    return p
    # Use time since Jan 1, 1970 in filename in order make
    # a unique filename that the browser has not chached
    

if __name__ == '__main__':
    print (compute(1,1,1))