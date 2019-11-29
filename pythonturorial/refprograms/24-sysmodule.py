'''
https://www.tutorialsteacher.com/python/sys-module
Python - Sys Module
The sys module provides functions and variables used to manipulate different parts of the Python runtime environment. 
You will learn some of the important features of this module here.
'''

'''
sys.argv returns a list of command line arguments passed to a Python script. The item at index 0 in this list is always the name of the script. 
The rest of the arguments are stored at the subsequent indices.
'''

import sys

print("Hello {}. Welcome to {} tutorial".format(sys.argv[1], sys.argv[2]))
print("0 argument ",sys.argv[0])


#import sys
user_input = sys.stdin.readline()
print("Input : " + user_input)

sys.exit(1)

print(sys.copyright)


variable = "JournalDev"

print(sys.getrefcount(0))
print(sys.getrefcount(variable))
print(sys.getrefcount(None))




'''
sys.exit
This causes the script to exit back to either the Python console or the command prompt. This is generally used to safely exit from the program in 
case of generation of an exception.


sys.exit(1)
print('After exit')


sys.maxsize
Returns the largest integer a variable can take.

print('max size ',sys.maxsize)


sys.path
This is an environment variable that is a search path for all Python modules.


print(' path ',sys.path)


sys.version
This attribute displays a string containing the version number of the current Python interpreter.


print('version ' ,sys.version)
'''