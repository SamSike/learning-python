pal=input("Enter String : ")
a=len(pal)-1
k=b=0
for c in pal:
    if pal[b]==pal[a]:
        k+=1
    a-=1
    b+=1
if k==len(pal):
    print("Palindrome")
else:
    print("Not Palindrome")
