from __future__ import print_function
import sys
print (sys.argv)
print (sys.version_info)
'''
if sys.version_info[0]<3:
    x=raw_input("Raw Enter : ")
else:
    x=input("Enter : ")
print (x)
'''
print (r'C:\some\name') 

print ("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
print ('''\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
''')
print(5*'\nsameer '+'is the boss')
print('Py' 'thon')
text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text)
word = 'Python'
print(word[0])
