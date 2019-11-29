import random

class account():
    def openAccount(self,name,email,mobile,idproof):
        self.name = name
        self.email = email
        self.mobile = mobile
        self.idproof = idproof
        self.accountno = random.randint(1000,10000)
        self.balance = 0
        return self.accountno
    
    def deposit(self,actno,amount):
        self.balance = self.balance + amount
        return self.balance
    
    def withdraw(self,actno,amount):
        self.balance = self.balance - amount
        return self.balance
    
    def checkBalance(self,actno):
        return self.balance
actholders = []
myact = account()
actholders.append(myact)

depamt = 10000
actno =myact.openAccount('raghu',9845547471,'prasadraghuks@gmail.com',986878888) 
bal = myact.deposit(actno,depamt) 
print('Balance after deposit of ',depamt, ' : ',bal)
depamt = 15000
bal = myact.deposit(actno,depamt) 
print('Balance after deposit of ',depamt, ' : ',bal)

myfriendact = account()
actholders.append(myfriendact)

depamt = 12000
actno =myfriendact.openAccount('ravi',9845547472,'raviks@gmail.com',986878999) 
bal = myfriendact.deposit(actno,depamt) 
print('Balance after deposit of ',depamt, ' : ',bal)
depamt = 18000
bal = myfriendact.deposit(actno,depamt) 
print('Balance after deposit of ',depamt, ' : ',bal)


  
        