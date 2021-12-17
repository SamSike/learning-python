Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=10
>>> x=10; y=20
>>> print (x); print (y)
10
20
>>> "our value is 10"
'our value is 10'
>>> print("Our Value Is ",x)
Our Value Is  10
>>> print("Our Value Is",x,"and",y)
Our Value Is 10 and 20
>>> a=b=c=1
>>> print(a,b,c)
1 1 1
>>> print(a,b,c,sep='')
111
>>> print(a,sep=' ',b,c)
SyntaxError: positional argument follows keyword argument
>>> print(a,b,c,sep='',end='*')
111*
>>> print(a,b,c,sep='',"*")
SyntaxError: positional argument follows keyword argument
>>> a,b,c=1,2,John
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a,b,c=1,2,John
NameError: name 'John' is not defined
>>> a,b,c=1,2,"John"
>>> print(a,b,c)
1 2 John
>>> a,b=1.2,3
>>> c[2]=3,5
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    c[2]=3,5
TypeError: 'str' object does not support item assignment
>>> number, list, string, dictionary, tuple - standard data types
SyntaxError: invalid syntax
>>> number - int, float, long, complex
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    number - int, float, long, complex
NameError: name 'number' is not defined
>>> str="Hello World"
>>> print (str)
Hello World
>>> print (str[0])
H
>>> print(a)
1.2
>>> print(str[2:6])
llo 
>>> print(str[2:7])
llo W
>>> print(str[2:],end="*")
llo World*
>>> print(str*2)
Hello WorldHello World
>>> print (str+"test")
Hello Worldtest
>>> print(str+ " 'No'")
Hello World 'No'
>>> for(b=0;b<5;b++)
SyntaxError: invalid syntax
>>> for c in str
SyntaxError: invalid syntax
>>> for c in "hello"
SyntaxError: invalid syntax
>>> for c in "hello":
	print(c)

	
h
e
l
l
o
>>> for c in str:
	print(c+"test")

	
Htest
etest
ltest
ltest
otest
 test
Wtest
otest
rtest
ltest
dtest
>>> b=str
>>> print(b)
Hello World
>>> a=0
>>> for index in range(len(str)):
	print(index)

	
0
1
2
3
4
5
6
7
8
9
10
>>> for c in range(len(str):
	       
SyntaxError: invalid syntax
>>> for c in range(len(str)):
	b[a+=1]=str[len(str)-=1]
	
SyntaxError: invalid syntax
>>> b=0
>>> c=len(str)
>>> for c in range(len(str)):
	
