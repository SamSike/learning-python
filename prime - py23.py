from __future__ import print_function
import sys
if sys.version_info[0]<3:
    n=raw_input("Enter Final Number to be printed : ")
else:
    n=input("Enter Final Number to be outputted : ")
n=eval(n)
def prime(x):
    a=2
    while a<x:
        k=0
        b=2
        while b<a:
            if (a%b)==0:
                k+=1
            b+=1
        if k==0:
            print(a)
        a+=1
prime(n)
