'''
It is possible to automatically perform many operating system tasks. The OS module in Python provides functions 
for creating and removing a directory (folder), fetching its contents, changing and identifying the current directory, etc.
'''
'''
We can create a new directory using the mkdir() function from the OS module.
'''

import os
os.mkdir("d:\\tempdir")

'''
Changing the Current Working Directory
'''
os.chdir("d:\\tempdir")
'''
Get current working directory
'''
os.getcwd()

'''
Removing a Directory
'''
os.rmdir("d:\\tempdir")

'''
List Files and Sub-directories
'''
os.listdir("d:\products")

os.listdir()
