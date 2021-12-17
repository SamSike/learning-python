from __future__ import print_function
import sys
if sys.version_info[0]<3:
    n=raw_input("Enter no of rows : ")
else:
    n=input("Enter no of Rows : ")
n=eval(n)
i=1
while i<=n:
    j=0
    while j<n-i:
        print(" ",end="")
        j+=1
    j=0
    while j<i:
        print("*",end="")
        j+=1
    print("")
    i+=1
