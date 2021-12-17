from __future__ import print_function
import sys
if sys.version_info[0]<3:
    n=raw_input("Enter Final Number to be printed : ")
else:
    n=input("Enter Final Number to be outputted : ")
n=eval(n)
def fib(x):
    a=b=c=1
    print(a)
    print(b)
    for c in range(x):
        c=a+b
        if c>x:
            break
        print(c)
        a=b
        b=c
fib(n)
