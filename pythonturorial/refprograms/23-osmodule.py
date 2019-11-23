'''
It is possible to automatically perform many operating system tasks. The OS module in Python provides functions 
for creating and removing a directory (folder), fetching its contents, changing and identifying the current directory, etc.
'''
'''
We can create a new directory using the mkdir() function from the OS module.
'''

import os
os.mkdir("d:\\test1")

'''
Changing the Current Working Directory
'''
os.chdir("d:\\test1")
'''
Get current working directory
'''
os.getcwd()

'''
Removing a Directory
'''
os.rmdir("d:\\test1")

'''
List Files and Sub-directories
'''
os.listdir("d:\products")

os.listdir()

#print(os.listdir("e:\kaushalya.tech\consultancy\active\python\pythonturorial\refprograms"))

print('Operating system name ', os.name)
print('Absolute path ', os.path.abspath('.'))
print('Files and directories ' ,os.listdir('.')) 

