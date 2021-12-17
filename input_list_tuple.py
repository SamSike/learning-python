from __future__ import print_function
import sys
if sys.version_info[0]<3:
    x=raw_input("Enter : ")
else:
    x=input("Enter: ")
print(x)
x=x.split(',')
print("List : ",x)
x=tuple(x)
print("Tuple : ",x)
