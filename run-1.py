Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s="hello"
>>> s.capitalise()
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    s.capitalise()
AttributeError: 'str' object has no attribute 'capitalise'
>>> s.capitalize()
'Hello'
>>> s="HELLO"
>>> s.capitalize()
'Hello'
>>> s="HELLO WORLD"
>>> s.capitalize()
'Hello world'
>>> s="HELLO WORLD. I AM SAMEER"
>>> s.capitalize()
'Hello world. i am sameer'
>>> s.center()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    s.center()
TypeError: center() takes at least 1 argument (0 given)
>>> s.center(10,'X')
'HELLO WORLD. I AM SAMEER'
>>> s.center(50,'*')
'*************HELLO WORLD. I AM SAMEER*************'
>>> s="lol"
>>> s.center(10,'X')
'XXXlolXXXX'
>>> s.center(100,' ')
'                                                lol                                                 '
>>> s.count('o')
1
>>> s.count('l')
2
>>> s
'lol'
>>> s="Hello World"
>>> s.count('o')
2
>>> s.count('o',0,5)
1
>>> s.count('o',5)
1
>>> s.count('l',5)
1
>>> s.encode(1)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    s.encode(1)
TypeError: encode() argument 1 must be str, not int
>>> s.encode('utf-8')
b'Hello World'
>>> s
'Hello World'
>>> s.encode('utf-5')
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    s.encode('utf-5')
LookupError: unknown encoding: utf-5
>>> s.endswith('World')
True
>>> s.endswith('world')
False
>>> s="äöü"
>>> s.encode('utf-8')
b'\xc3\xa4\xc3\xb6\xc3\xbc'
>>> s="Hello123"
>>> s.isalnum()
True
>>> s.istitle()
True
>>> s.ljust(70,'*')
'Hello123**************************************************************'
>>> s.rjust(70,'*')
'**************************************************************Hello123'
>>> s.center(70,'*')
'*******************************Hello123*******************************'
>>> ("%d is my marks at 10th %s")%(100,"grade")
'100 is my marks at 10th grade'
>>> print('%(language)s has %(number)03d quote types.' %{'language': "Python", "number": 2})
Python has 002 quote types.
>>> print('%(language)s has %(number)X3d quote types.' %{'language': "Python", "number": 2})
Python has 23d quote types.
>>> print('%(language)s has %(number)*3d quote types.' %{'language': "Python", "number": 2})
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    print('%(language)s has %(number)*3d quote types.' %{'language': "Python", "number": 2})
TypeError: not enough arguments for format string
>>> print('%(language)s has %(number)05d quote types.' %{'language': "Python", "number": 2})
Python has 00002 quote types.
>>> print('%(language)s has %(number)'*'3d quote types.' %{'language': "Python", "number": 2})
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    print('%(language)s has %(number)'*'3d quote types.' %{'language': "Python", "number": 2})
TypeError: can't multiply sequence by non-int of type 'str'
>>> print('%(language)s has %(number)"*"3d quote types.' %{'language': "Python", "number": 2})
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    print('%(language)s has %(number)"*"3d quote types.' %{'language': "Python", "number": 2})
ValueError: unsupported format character '"' (0x22) at index 26
>>> print('%(language)s has %(number)\'*\'3d quote types.' %{'language': "Python", "number": 2})
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    print('%(language)s has %(number)\'*\'3d quote types.' %{'language': "Python", "number": 2})
ValueError: unsupported format character ''' (0x27) at index 26
>>> print('%(language)s has %(number)"Y"3d quote types.' %{'language': "Python", "number": 2})
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    print('%(language)s has %(number)"Y"3d quote types.' %{'language': "Python", "number": 2})
ValueError: unsupported format character '"' (0x22) at index 26
>>> print('%(language)s has %(number)'Y'3d quote types.' %{'language': "Python", "number": 2})
SyntaxError: invalid syntax
>>> print('%(language)s has %(number)\'Y\'3d quote types.' %{'language': "Python", "number": 2})
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    print('%(language)s has %(number)\'Y\'3d quote types.' %{'language': "Python", "number": 2})
ValueError: unsupported format character ''' (0x27) at index 26
>>> print('%(language)s has %(number) 3d quote types.' %{'language': "Python", "number": 2})
Python has   2 quote types.
>>> print('%(language)s has %(number)A3d quote types.' %{'language': "Python", "number": 2})
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    print('%(language)s has %(number)A3d quote types.' %{'language': "Python", "number": 2})
ValueError: unsupported format character 'A' (0x41) at index 26
>>> print('%(language)s has %(number)Y3d quote types.' %{'language': "Python", "number": 2})
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    print('%(language)s has %(number)Y3d quote types.' %{'language': "Python", "number": 2})
ValueError: unsupported format character 'Y' (0x59) at index 26
>>> print('%(language)s has %(number)93d quote types.' %{'language': "Python", "number": 2})
Python has                                                                                             2 quote types.
>>> print('%(language)s has %(number)33d quote types.' %{'language': "Python", "number": 2})
Python has                                 2 quote types.
>>> print('%(language)s has %(number)21d quote types.' %{'language': "Python", "number": 2})
Python has                     2 quote types.
>>> print('%(language)s has %(number)03d quote types.' %{'language': "Python", "number": 2})
Python has 002 quote types.
>>> print('%(language)s has %(number)3d quote types.' %{'language': "Python", "number": 2})
Python has   2 quote types.
>>> 
=============== RESTART: D:/New Century Computers/Python/t.py ===============
2
3
4
5
6
7
8
9
Else
>>> 
