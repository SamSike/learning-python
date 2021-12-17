from __future__ import print_function
import sys
if sys.version_info[0]<3:
    n=raw_input("Enter Number of Rows to be printed : ")
else:
    n=input("Enter Number of Rows to be outputted : ")
n=eval(n)
a=1
while a<=n:
    b=1
    while b<=a:
        print(a,end="")
        b+=1
    print("")
    a+=1
