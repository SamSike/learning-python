Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:37:19) [MSC v.1500 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s="Hello"
>>> s.lower()
'hello'
>>> s.upper()
'HELLO'
>>> print(s)
Hello
>>> s=s.upper()
>>> print(s)
HELLO
>>> s="   Hello World    "
>>> s.strip()
'Hello World'
>>> s="   Hello            World     "
>>> print(s)
   Hello            World     
>>> s.strip()
'Hello            World'
>>> s.isaplha()

Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    s.isaplha()
AttributeError: 'str' object has no attribute 'isaplha'
>>> s.isalpha()
False
>>> s="Hello"
>>> s.isalpha()
True
>>> x=(2,3)
>>> x.isdigit()

Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    x.isdigit()
AttributeError: 'tuple' object has no attribute 'isdigit'
>>> s="1,2,3"
>>> s="123"
>>> s.isdigit()
True
>>> s="Hello "
>>> s.isalpha()
False
>>> s.isspace()
False
>>> s=" "
>>> s.isspace()
True
>>> s="hello"
>>> s.startswith("hell")
True
>>> s=" Hello"
>>> s.startswith(" ")
True
>>> s=" Hello "
>>> s.endswith(" ")
True
>>> s.find(" ")
0
>>> s.find("Hello")
1
>>> s.find("o")
5
>>> s.find("z")
-1
>>> s.replace("o","p")
' Hellp '
>>> s.replace(" ","A")
'AHelloA'
>>> s.replace(" ","XCV")
'XCVHelloXCV'
>>> s="1,2,3"
>>> s.split(",")
['1', '2', '3']
>>> s=raw_input("Enter : ")
Enter : 2,3,4,5,6
>>> s.split(",")
['2', '3', '4', '5', '6']
>>> l=s.split(",")
>>> type(l)
<type 'list'>
>>> print(l)
['2', '3', '4', '5', '6']
>>> t=tuple(l)
>>> t=print(t)
SyntaxError: invalid syntax
>>> print(t)
('2', '3', '4', '5', '6')
>>> print(s)
2,3,4,5,6
>>> s.join(l)
'22,3,4,5,632,3,4,5,642,3,4,5,652,3,4,5,66'
>>> s="1"
>>> s.join(l)
'213141516'
>>> l=(0,0,0,0,0,1)
>>> s.join(l)

Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    s.join(l)
TypeError: sequence item 0: expected string, int found
>>> l=[0,0,0,0,1]
>>> s.join(l)

Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    s.join(l)
TypeError: sequence item 0: expected string, int found
>>> l=['0','0','0','1']
>>> s.join(l)
'0101011'
>>> ','.join(l)
'0,0,0,1'
>>> s='X'.join(l)
>>> print(s)
0X0X0X1
>>> l=s.split("X")
>>> print(l)
['0', '0', '0', '1']
>>> text = "%d little pigs come out, or I'll %s, and I'll %s, and I'll blow your %s down." % (3, 'huff', 'puff', 'house')
>>> text
"3 little pigs come out, or I'll huff, and I'll puff, and I'll blow your house down."
>>> text
"3 little pigs come out, or I'll huff, and I'll puff, and I'll blow your house down."
>>> HEllo

Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    HEllo
NameError: name 'HEllo' is not defined
>>> text
"3 little pigs come out, or I'll huff, and I'll puff, and I'll blow your house down."
>>> l.append('1,2,3')
>>> l
['0', '0', '0', '1', '1,2,3']
>>> l.extend(['4,5'])
>>> l
['0', '0', '0', '1', '1,2,3', '4,5']
>>> l.extend(['6','7'])
>>> l
['0', '0', '0', '1', '1,2,3', '4,5', '6', '7']
>>> l.append(l)
>>> l
['0', '0', '0', '1', '1,2,3', '4,5', '6', '7', [...]]
>>> l.extend(l)
>>> l
['0', '0', '0', '1', '1,2,3', '4,5', '6', '7', [...], '0', '0', '0', '1', '1,2,3', '4,5', '6', '7', [...]]
>>> l=['1','2','3']
>>> l.insert(0,'0')
>>> l
['0', '1', '2', '3']
>>> l.insert(5,'5')
>>> l
['0', '1', '2', '3', '5']
>>> l.index('3')
3
>>> l.index('5')
4
>>> l.remove('5')
>>> l
['0', '1', '2', '3']
>>> l.append('1')
>>> l
['0', '1', '2', '3', '1']
>>> l.remove('1')
>>> l
['0', '2', '3', '1']
>>> l.pop(1)
'2'
>>> l
['0', '3', '1']
>>> l.pop()
'1'
>>> l
['0', '3']
>>> l.push('1')

Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    l.push('1')
AttributeError: 'list' object has no attribute 'push'
>>> l
['0', '3']
>>> l.append('1')
>>> l
['0', '3', '1']
>>> l1=[]
>>> l1
[]
>>> l1.append('1')
>>> l1
['1']
>>> l1.append(1)
>>> l1
['1', 1]
>>> l1.append(l)
>>> l1
['1', 1, ['0', '3', '1']]
>>> l.pop(2)
'1'
>>> l
['0', '3']
>>> l1.pop()
['0', '3']
>>> l1
['1', 1]
>>> 
