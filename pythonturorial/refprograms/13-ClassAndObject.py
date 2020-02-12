#Class
class myClass():    
    def method1(self):
        print("myClass:method1")
    def method2(self, name):
        print("myClass:method2:Name " , name)
    '''
    def method3():
        print('without self',name)
    '''
mycls = myClass()
mycls.method1()
mycls.method2("Python")

mycls1 = myClass()
mycls1.method1()
mycls1.method2("Machine Learning")
def main1():
    # exercise the class methods
    c = myClass()
    c.method1()
    c.method2("Python")    
    c1 = myClass()
    c1.method1()
    c1.method2("Machine Learning")
if (__name__ == "__main__"):
    main1()
    
class student():
    def register(self,regno,name,standard,section):        
        self.regno = regno
        self.name = name
        self.standard = standard
        self.section = section        
    def information(self):
        print('Regno ',self.regno,' Name ',self.name,' Standard ',self.standard,' Section ',self.section)
        
bhavikaa = student()
bhavikaa.register(101,'Bhavikaa','9','A')
bhavikaa.information()
shloka = student()
shloka.register(102,'Shloka','9','C')
shloka.information()

print('Enter student information')
regno = int(input('Enter Registration Number'))
name = input('Enter your name')
std = int(input('Enter your standard'))
sec = input ('Enter your section')
newstd = student()
newstd.register(regno,name,std,sec)
newstd.information()
   
class Animal():
    def eat(self):
        print('Eating')        
class Dog(Animal):
    def bark(self):
        print('Barking')
d= Dog()
d.eat()
d.bark()
#Multi level
class Animal:
    def eat(self):
        print('Eating')
class Dog(Animal):
    def bark(self):
        print('Barking')
class BabyDog(Dog):
    def weep(self):
        print('Weeping ')
d= BabyDog()
d.eat()
d.bark()
d.weep()

#Inheritance
class myClass():
    def method1(self):
        print("Parent:method1")
    def method2(self, name):
        print("Parent Method 2 :",name)
    def method3(self,city):
        print ("You are from ", city)
#class childClass():
class childClass(myClass):
    def method1(self):
        myClass.method1(self)
        print("ChildClass:method1")
    def method2(self):
        print("childClass:method2")
'''
def main():
    # exercise the class methods
    c2 = childClass()
    c2.method1()
    c2.method2()
    c2.method3("Bengaluru")
if (__name__ == "__main__"):
    main()
    
'''    
c2 = childClass()
c2.method1()
c2.method2()
c2.method3("Bengaluru")
class Bank():
   def __init__(self,name,address,noOfBranch):
       print('init of bank')
       self.name = name
       self.address = address
       self.noOfBranch = noOfBranch
       print ('bank details :name ',self.name,' address : ',self.address,' no of branches ',self.noOfBranch )
   def Bank(self):
       print('tesing')       
   def rateOfInterest(self):       
       return 0   
   def calculateInterest(self,p,r,t):
       return p*r*t/100

class SBI(Bank):
   def __init__(self,name,address,noOfBranch):
       print('init of sbi')
       Bank.__init__(self,name,address,noOfBranch)       
   def rateOfInterest(self):
       print('interest rate of sbi')
       return 6

class Karnataka(Bank):
    '''
    def __init__(self,name,address,noOfBranch):
        print('init of Karnataka')
        Bank.__init__(self,name,address,noOfBranch)
    '''   
    def rateOfInterest(self):
        print('interest rate of Karnataka')
        return 6.5

sbi = SBI('State Bank of India','Nariman point,Mumbai',1000)
roi = sbi.rateOfInterest()
interest =sbi.calculateInterest(100000,roi,1)
print('interest from sbi is ',interest)
 
kar = Karnataka('Karnataka Bank','Nehru Road,Mangaluru',1003)
roi = kar.rateOfInterest()
interest =kar.calculateInterest(100000,roi,1)
print('interest from karnataka bank is ',interest)

bnk = Bank('RBI','Delhi',10)
bnk.Bank()


import random
class Account():
    def openAccount(self,name,mobile,email,idproof):
        self.name = name
        self.mobile = mobile
        self.email = email
        self.idproof = idproof
        self.balance = 0
        self.accountno = random.randint(100,10000)
        return self.accountno    
    def deposit(self,actno,amount):
        self.balance = self.balance + amount
        return self.balance        
    def withdraw(self,actno,amount):
        self.balance = self.balance - amount
        return self.balance    
    def checkBalance(self,actno):
        return self.balance

raghuact = Account()
actno = raghuact.openAccount('raghu',9845547471,'prasadraghuks@gmail.com',99393939393)
print('Account no ',actno)
depamt1 = 10000
bal = raghuact.deposit(actno,depamt1)
print('Balance after deposit of ',depamt1, ' is ',bal)
depamt2 = 15000
bal = raghuact.deposit(actno,depamt2)
print('Balance after deposit of ',depamt2, ' is ',bal)
withdrawamt1 = 7000
bal = raghuact.withdraw(actno,withdrawamt1)
print('Balance after withdrawal of ',withdrawamt1, ' is ',bal)
bal = raghuact.checkBalance(actno)
print('Checking the balance ',bal)

import random
class exam():
    def addStudent(self,name,course):
        self.name = name
        self.course = course
        self.regno = random.randint(1000,5000)
        self.examlist =[]
        self.total = 0
        return self.regno
    
    def addmarks(self,regno,sub,marks):
        studict = {}
        studict['regno'] = regno
        studict[sub] = marks
        self.examlist.append(studict)
        
    def display(self,regno):

        for info in self.examlist:
            print('dictionary ',info)
            if (info['regno'] == regno):
                for k,v in info.items():
                    print(k,v)
                    if (k!='regno'):
                        self.total = self.total + int(v)
        print('total ' ,self.total)
raghu = exam()
regno = raghu.addStudent('raghu','python master class')
print('reg no ',regno)
raghu.addmarks(regno,'basic',80)
raghu.addmarks(regno,'intermediate',70)
raghu.addmarks(regno,'advanced',70)
raghu.display(regno)

n=8/10

class vehicle():
    def __init__(self,make,model,color,price):
        self.make = make
        self.model = model
        self.color = color
        self.price = price
        self.speed = 0
    
    def start(self):
        pass
    
    def speed(self):
        pass
    
    def stop(self):
        print('stop')
    
    def info(self):
        print('vehicle details : make - {} , model -{},color -{},price - {}'.format(self.make,self.model,self.color,self.price) )
    
class bike(vehicle):
    def start(self):
        self.speed = 0
        print('Bike- Kick start')
    
    def speedofvehicle(self):
        self.speed = self.speed + 5
        return self.speed
    
    def stop(self):
        self.speed = 0
        print('stop')

hero = bike('hero','star','black',60000)
hero.info()
hero.start()
currspeed = hero.speedofvehicle()
print('current speed 1',currspeed)
currspeed = hero.speedofvehicle()
print('current speed 2',currspeed)

hero.stop()


class student():
    def __init__(self,regno,name,standard,section,marks):        
        self.regno = regno
        self.name = name
        self.standard = standard
        self.section = section
        self.marks = marks        
    def information(self):
        print('Regno ',self.regno,' Name ',self.name,' Standard ',self.standard,' Section ',self.section, ' marks : ',self.marks)


stud = student(103,'Satvik',10,'A',500)

studlist = []
noofstudents=int(input("Enter no of students"))
for n in range(noofstudents):
    regno = input("enter registration number")
    name = input("enter name")
    standard = input("enter standard")
    section = input("enter section")
    marks = int(input("enter marks"))
    stud = student(regno,name,standard,section,marks)
    studlist.append(stud)

max = 0
index = 0
mindex = 0
for s in studlist:
    #print(s.information())
    if (s.marks > max):
        max = s.marks
        mindex = index
        
    index = index + 1

print('maximum marks ',max)
print('student scoring maximum marks ',studlist[mindex].name)
    
'''
Method overloading
'''

class passport():
    def validdocumentsDOB(self,BC=None,tenthmarkscard=None,aadhar=None):
        if(BC):            
            print('You have provided Birth certificate as valid document')            
        if(tenthmarkscard):
            print('You have provided Tenth standard marks card as valid document')
        if(aadhar):            
            print('You have provided Aadhar standard marks card as valid document')
        if (BC==None and tenthmarkscard==None and aadhar==None ):
            print('You have not provided valid document/s')
    def validdocumentforAddress(self,Telephone,passport,rationcard):
        print('it is mandaroty')

passportobj = passport()
passportobj.validdocumentsDOB('BC')
passportobj.validdocumentsDOB('BC','10 th markscard')
passportobj.validdocumentsDOB('BC','10 th markscard',909999999)
passportobj.validdocumentsDOB()
passportobj.validdocumentforAddress('0000999')

'''
java


class passport():
    def validdocumentsDOB(self,BC=None):
        if(BC):            
            print('You have provided Birth certificate as valid document')            
        if (BC==None ):
            print('You have not provided valid document/s')

    def validdocumentsDOB(self,tenthmarkscard=None):
        if(tenthmarkscard):
            print('You have provided Tenth standard marks card as valid document')
        if (BC==None and tenthmarkscard==None and aadhar==None ):
            print('You have not provided valid document/s')

'''  
class Calculator ():
    def add(self,n1,n2):
        return n1 + n2
    
    
calc = Calculator()
result = calc.add(100,30)
print ('Result ',result)
      