#Function
def func1():
    print('I am learning python  function')
    
func1()
#Square
def square(x):
    y = x*x
    print('Square of : ',x,'is ', y)
square (3)
#Square with return value
def square(x):
    y=x*x
    return y
z=square(4)
print('Square:Return Value', z)
print('Square of 5:Return Value ', square(5))
#Function Arguments
def multiply(num1,num2):
    print(' num1 :', num1, ' num2 :', num2)
    return num1*num2
product = multiply(10,12)
print('product : ',product)
product = multiply(num2=10,num1=15)
print('product : ',product)
#Function with multiple arguments
def multiple(*args):
    print(args)
    print(args[0])
    print(args[1])
    
multiple(1,3,4,5,7,9,10)
multiple(4,5)


# Write a function to calculate simple interest

# i = prt/100

# Write a function to convert from fahrenheit to celcius
#Celsius to Fahrenheit:   (°C × 9/5) + 32 = °F
#Fahrenheit to Celsius:   (°F − 32) x 5/9 = °C
def simpleInterest(p,r,t):
    i = (p*r*t)/100;
    return i;
interest = simpleInterest(1000,6,1)
#print('Simple interest is ',interest)
p = float(input('Enter principal amount'))
r = float(input('Enter Rate of interest'))
t = float(input('Enter Time in year'))
interest = simpleInterest(p,r,t)
print('Simple interest is ',interest)
name =input('enter your name')
print('your name is ',name)

''''
Python pass statement

You can consider python pass statement as no operation statement. The difference between Python 
comments and pass statement is; comments are being eliminated while interpreting the program 
but pass statement does not. It consumes execution cycle like a valid statement. 
For example, for printing only the odd numbers from a list, our program flow will be:
'''


#Generate a list of number
numbers = [ 1, 2, 4, 3, 6, 5, 7, 10, 9 ]
#Check for each number that belongs to the list
for number in numbers:
        #check if the number is even
	if number % 2 == 0:
                #if even, then pass ( No operation )
                pass
	else:
                #print the odd numbers
		print (number)

'''
In Python, we can pass a variable number of arguments to a function using special 
symbols. There are two special symbols:

*args (Non Keyword Arguments)
**kwargs (Keyword Arguments)
'''

def adder(*num):
    print("type ",type(num))
    sum = 0
    
    for n in num:
        sum = sum + n
    print("Sum:",sum)
adder(3,5)
adder(4,5,6,7)
adder(1,2,3,5,6)

def intro(**data):
    print("\nData type of argument:",type(data))
    for key, value in data.items():
        print("{} is {}".format(key,value))
intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)


def factorial(n):    
    if n == 1:
        print(n)
        return 1    
    else:
        print (n,'*', end=' ')
        return n * factorial(n-1)
factorial(5)


