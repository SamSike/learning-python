import sys
x=input("Enter Number : ")
if sys.version_info[0]>=3:
    x=eval(x)
def armstrong(value):
    b=0
    c=value
    while value>0:
        a=value%10
        a=a**3
        b+=a
        value//=10
    if b==c:
        print(c," is an Armstrong Number")
i=1
while i<=x:
    armstrong(i)
    i+=1
