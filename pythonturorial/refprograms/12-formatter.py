# -*- coding: utf-8 -*-

#https://www.geeksforgeeks.org/python-format-function/

'''
Code #1 : Simple demonstration of format().
'''
# Python3 program to demonstarte 
# the str.format() method 

# using format option in a simple string 
print ("{}, A computer science portal for geeks."
						.format("GeeksforGeeks")) 
# using format option for a 
# value stored in a variable 
str = "This article is written in {}"
print (str.format("Python")) 

# formatting a string using a numeric constant 
print ("Hello, I am {} years old !".format(18)) 


'''
Output :
GeeksforGeeks, A computer science portal for geeks.
This article is written in Python
Hello, I am  18 years old!

'''
'''
Code #2 :
'''

# Python program demonstrating Index error 

# Number of placeholders are four but 
# there are only three values passed 

# parameters in format function. 
my_string = "{}, is a {} {} science portal for {}"

print (my_string.format("GeeksforGeeks", "computer", "geeks")) 


'''
Code #3 : Formatters with multiple place holders.
'''
# Python program using multiple place 
# holders to demonstrate str.format() method 

# Multiple placeholders in format() function 
my_string = "{}, is a {} science portal for {}"
print (my_string.format("GeeksforGeeks", "computer", "geeks")) 

# different datatypes can be used in formatting 
print ("Hi ! My name is {} and I am {} years old"
							.format("User", 19)) 

# The values passed as parameters 
# are replaced in order of their entry 
print ("This is {} {} {} {}"
	.format("one", "two", "three", "four")) 

'''
Output :
GeeksforGeeks, is a computer science portal for geeks
Hi! My name is User and I am 19 years old
This is one two three four
'''

'''
Code #4 :Formatters with Positional and Keyword Arguments :
'''

# To demonstrate the use of formatters 
# with positional key arguments. 

# Positional arguments 
# are placed in order 
print("{0} love {1}!!".format("GeeksforGeeks", 
									"Geeks")) 

# Reverse the index numbers with the 
# parameters of the placeholders 
print("{1} love {0}!!".format("GeeksforGeeks", 
									"Geeks")) 


print("Every {} should know the use of {} {} programming and {}"
	.format("programmer", "Open", "Source", "Operating Systems")) 
# Use the index numbers of the 
# values to change the order that 
# they appear in the string 
print("Every {3} should know the use of {2} {1} programming and {0}"
		.format("programmer", "Open", "Source", "Operating Systems")) 
# Keyword arguments are called 
# by their keyword name 
print("{gfg} is a {0} science portal for {1}"
.format("computer", "geeks", gfg ="GeeksforGeeks")) 
'''
Type Specifying :
More parameters can be included within the curly braces 
of our syntax. Use the format code syntax 
{field_name:conversion}, 
where field_name specifies the 
index number of the argument to 
the str.format() method, and 
conversion refers to the conversion 
code of the data type.
'''
'''
s – strings
d – decimal integers (base-10)
f – floating point display
c – character
b – binary
o – octal
x – hexadecimal with lowercase letters after 9
X – hexadecimal with uppercase letters after 9
e – exponent notation
'''

'''
#Code 5
'''

# Demonstrate ValueError while 
# doing forced type-conversions 

# When explicitly converted floating point 
# values to decimal with base-10 by 'd' 
# type conversion we encounter Value-Error. 
'''print("The temperature today is {0:d} degrees outside !"
										.format(35.567)) 
'''

# Instead write this to avoid value-errors 
print("The temperature today is {0:.2f} degrees outside !"
											.format(35.567))

print("{0:6.2f}".format(99.938))
print("{0:10.2f}".format(99.938))


'''
Code #6 :
'''

# Convert base-10 decimal integers 
# to floating point numeric constants 
print ("This site is {0:f}% securely {1}!!". 
					format(100, "encrypted")) 

# To limit the precision 
print ("My average of this {0} was {1:.2f}%"
			.format("semester", 78.234876)) 

# For no decimal places 
print ("My average of this {0} was {1:.0f}%"
			.format("semester", 78.234876)) 

# Convert an integer to its binary or 
# with other different converted bases. 
print("The {0} of 100 is {1:b}"
		.format("binary", 100)) 
		
print("The {0} of 100 is {1:o}"
		.format("octal", 100)) 
'''
Padding Substitutions or Generating Spaces :
Code #7 :

By default strings are left-justified within the field, 
and numbers are right-justified. We can modify this by 
placing an alignment code just following the colon.

<   :  left-align text in the field
^   :  center text in the field
>   :  right-align text in the field
'''

# To demonstrate spacing when 
# strings are passed as parameters 
print("{0:4}, is the computer science portal for {1:8}!"
						.format("GeeksforGeeks", "geeks")) 

print("{0:10}.. is my {1:10}...!".format("India","country"))
print("{0:8}..".format("python"))


# To demonstrate spacing when numeric 
# constants are passed as parameters. 
print("It is {0:5} degrees outside !"
						.format(40)) 

# To demonstrate both string and numeric 
# constants passed as parameters 
print("{0:4} was founded in {1:16}!"
	.format("GeeksforGeeks", 2009)) 

# To demonstrate aligning of spaces 
print("{0:*^16} was founded in {1:#<8}!"
		.format("GeeksforGeeks", 2009)) 

print("{:*^20}".format("Geeks")) 

'''
GeeksforGeeks, is the computer science portal for geeks   !
It is    40 degrees outside!
GeeksforGeeks was founded in             2009!
 GeeksforGeeks   was founded in 2009 !
*******Geeks********
'''

'''
Applications :
Formatters are generally used to Organize Data. Formatters can be seen in their best light when they are being used to organize a lot of data in a visual way. If we are showing databases to users, using formaters to increase field size and 
modify alignment can make the output more readable.
'''

# which prints out i, i ^ 2, i ^ 3, 
# i ^ 4 in the given range 

# Function prints out values 
# in an unorganized manner 
def unorganized(a, b): 
	for i in range (a, b): 
		print ( i, i**2, i**3, i**4 ) 
unorganized(0,5)

# Function prints the organized set of values 
def organized(a, b): 
	for i in range (a, b): 
organized(0,5)
		# Using formatters to give 6 
		# spaces to each set of values 
		print("{:6d} {:6d} {:6d} {:6d}"
		.format(i, i ** 2, i ** 3, i ** 4)) 

# Driver Code 
n1 = int(input("Enter lower range :-\n")) 
n2 = int(input("Enter upper range :-\n")) 

print("------Before Using Formatters-------") 

# Calling function without formatters 
unorganized(n1, n2) 

print() 
print("-------After Using Formatters---------") 
print() 

# Calling function that contain 
# formatters to organize the data 
organized(n1, n2) 

'''
Output :


Enter lower range :-
3
Enter upper range :-
10
------Before Using Formatters-------
3 9 27 81
4 16 64 256
5 25 125 625
6 36 216 1296
7 49 343 2401
8 64 512 4096
9 81 729 6561

-------After Using Formatters---------

     3      9     27     81
     4     16     64    256
     5     25    125    625
     6     36    216   1296
     7     49    343   2401
     8     64    512   4096
     9     81    729   6561

'''

print("{0:*^10}".format("hello"))
#**hello***
print("{0:*^10d}".format(1234))
#***1234***