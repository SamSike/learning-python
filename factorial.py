import sys
def fact(x):
    a=b=1
    while a<=x:
        b*=a
        a+=1
    print(b)
l=input("Enter Number : ")
if sys.version_info[0]>=3:
    l=eval(l)
fact(l)
