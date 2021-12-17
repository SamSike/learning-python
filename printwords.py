#the quick brown fox jumps over the lazy dog
from __future__ import print_function
import sys
def m1(str):
    a=str.split(' ')
    i=1
    while a:
        c=a.pop(0)
        if c=='':
            continue
        print(i,".",c)
        i+=1
if sys.version_info[0]<3:
    x=raw_input("Enter String : ")
else:
    x=input("Enter String : ")
m1(x)
