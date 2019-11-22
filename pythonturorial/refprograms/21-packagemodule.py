'''
https://www.tutorialsteacher.com/python/python-package
'''
'''
Python - Creating and Installing a Package
'''
'''
We organize a large number of files in different folders and 
subfolders based on some criteria, so that we can find and manage 
them easily. In the same way, a package in Python takes the concept 
of the modular approach to next logical level. As you know, a module 
can contain multiple objects, such as classes, functions, etc. A package 
can contain one or more relevant modules. Physically, 
a package is actually a folder containing one or more module files.
'''

'''
Create a new folder named D:\MyApp.
Inside MyApp, create a subfolder with the name 'mypackage'.
Create an empty __init__.py file in the mypackage folder.
Using a Python-aware editor like IDLE, create modules greet.py and 
functions.py with following code:
'''

'''
Importing a Module from a Package
Now, to test our package, invoke the Python prompt from the MyApp folder.
'''
'''
Install a Package Globally
Once a package is created, it can be installed for system wide use by running the setup script. 
The script calls setup() function from setuptools module.
'''