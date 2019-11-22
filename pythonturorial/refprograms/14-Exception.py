#with out expection handling

check = input('Enter data')
print ('check ',check)
n = int(input('Enter a number to validate division by zero'))

div = 100/n

print('result is ',div)


d = int(input('Enter a number to validate division by zero'))
try:
    a=10/d
    print(a)
except ArithmeticError:
    print("This statement is raising an exception")
else:
    print("No exception proceed")

print ('after the exception')
#Except with no exception

try:
    a=10/'a'
    print(a)
except:
    print("Exception")
else:
    print("Proceed no exception")

#Declaring multiple exception
try:
    a=10/0
    a=10/'raghu'
    print(a)
#except ArithmeticError,NameError: - 3.6 does not support
except ZeroDivisionError:
    print("ZeroDivisionError")
except ArithmeticError:
    print("ArithmeticError")
except:
    print("Generic Error")
else:
    print("Successfully Done")
#Finally Block

try:
    a=10/0;
    a=10/2;
    print(a)
except ZeroDivisionError:
    print(ZeroDivisionError)
finally:
    print("Finally block is always called")

#Raise an exception

try:
    a=10
    print(a)
    raise NameError("Hello")
except NameError as e:
    print("An exception occured")
    print(e)
#Custom exception
class ErrorInCode(Exception):
    def __init__(self,data):
     self.data = data
    def __str__(self):
        return repr('Error Code ' +str(self.data))
try:
    raise ErrorInCode(2000)
except ErrorInCode as ae:
#except ErrorInCode:
    print("Received error :",ErrorInCode)
    print("Received error :",ae)

class Student(object):
	def __init__(self, name, age, twitter_url=None, google_plus=None, youtube_channel=None):
		self.name = name
		self.age = age
		self.twitter_url = twitter_url
		self.google_plus = google_plus
 #       self.youtube_channel = youtube_channel

	def __str__(self):
		# Override to print a readable string presentation of your object
		# below is a dynamic way of doing this without explicity constructing the string manually
		return ', '.join(['{key}={value}'.format(key=key, value=self.__dict__.get(key)) for key in self.__dict__])

student = Student(name='Jone', age=23, twitter_url='http://twitter.com/jone')
print(student)

class InvalidAge(object):
#class InvalidAge(Exception):
    def __init__(self,data):
     self.data = data
    
    def __str__(self):
        print('over riding str')
        #return repr('Invalid Age ' +str(self.data))
        return 'Invalid age '
    '''
    def __repr__(self):
        print('overriding repr')
    '''    
age = int(input ('Enter your age'))
if (age >= 18):
    print('you are eligible to vote')
else:
    print('you are not eligible to vote')
    raise InvalidAge(age) 
    
    
class InvalidMarks(Exception):
    def __init__(self,data):
     self.data = data
    def __str__(self):
        return repr('Invalid marks ' +str(self.data))
    
marks=int(input('Enter your marks '))
if(marks<0 or marks>100):
    print('Marks is invalid ')
    raise  InvalidMarks(marks)
else:
    print('Marks is valid')


class InsufficientBal(Exception):
    def __init__(self,actno,amt):
        self.actno = actno
        self.amt = amt
    def __str__(self):
        return repr('Insufficient balance ' +str(self.amt))
    
 

    
class Account():
    def __init__(self,actno,name,mobile,email,idproof):
        self.actno = actno
        self.actno=actno
        self.mobile = mobile
        self.email = email
        self.idproof = idproof
        self.balance = 0
        
    def deposit(self,actno,amt):   
        self.balance = self.balance + amt
        return self.balance
    
    def withdraw(self,actno,amt):
        if (amt > self.balance):
            raise InsufficientBal(actno,amt)
        else:
            self.balance = self.balance - amt
        return self.balance
    
myact = Account(101,'raghu',9845547471,'prasadraghuks@gmail.com','adhar')
bal = myact.deposit(101,30000)

bal = myact.withdraw(101,35000)

print('after initial deposit',bal)

# REPR
#https://www.journaldev.com/22460/python-str-repr-functions

class Person:
    name = ""
    age = 0

    def __init__(self, personName, personAge):
        self.name = personName
        self.age = personAge

p = Person('Pankaj', 34)

print(p.__str__())
print(p.__repr__())



class Person:
    name = ""
    age = 0

    def __init__(self, personName, personAge):
        self.name = personName
        self.age = personAge

   
    def __repr__(self):
        return '{name:'+self.name+', age:'+str(self.age)+ '}'

    '''
    def __str__(self):
        return 'Person(name='+self.name+', age='+str(self.age)+ ')'
    '''

p = Person('Pankaj', 34)

# __str__() example
print(p)
print(p.__str__())

s = str(p)
print(s)

# __repr__() example
print(p.__repr__())
print(type(p.__repr__()))
print(repr(p))

x = object()

print(dir(x))



