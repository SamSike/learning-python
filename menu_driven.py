import sys
print("1. Prime Numbers\n2. Factorial\n3. Armstrong Numbers\n4. Exit")
ch=input("Enter your choice : ")
x=input("Enter Number for operation : ")
if sys.version_info[0]>=3:
    ch=eval(ch)
    x=eval(x)
if ch==1:
    prime(x)
elif ch==2:
    fact(x)
elif ch==3:
    armstrong(x)
elif ch==4:
    print("")
else:
    print("Invalid Number")
    menu_driven()
    
