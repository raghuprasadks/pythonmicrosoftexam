
counter = 0
import random

addrlist = []
class Address():    
    def __init__(self,addressline,city,zipcode,state):
        #self.addressline = addressline
        self.setaddressline(addressline)
        #self.city = city
        self.setcity(city)
        self.zipcode = zipcode
        self.state = state
        self.addressid = random.randint(1,1000)
        
    def getaddressid(self):
        return self.addressid    
    def setaddressline(self,addressline):
        self.addressline = addressline        
    def getaddressline(self):
        return self.addressline
    def setcity(self,city):
        self.city = city        
    def getcity(self):
        return self.city
    
    def validatezipcode(self,zipcode):
        isValid = True        
        if (len(zipcode) != 6):
            isValid = False
        if (zipcode.isdigit() == False):
            isValid = False
        
        return isValid
    

class Customer():
    def __init__(self,customername,telephonenumber,address):        
        global counter
        counter = counter + 1
        custid = 'C00'+str(counter)
        self.setcustomerid(custid)
        #self.customerid = 'C00'+str(counter)
        
        self.customername = customername
        self.telephonenumber = telephonenumber
        if (self.validateAddress(address) > 0):
            self.address = address
            addrlist.append(self.address)
            
        else:
            print('duplicate address')
            
    def setcustomerid(self,customerid):
        self.customerid = customerid        
    def getcustomerid(self):
        return self.customerid
    
    def setcustomername(self,customername):
        self.customername = customername        
    def getcustomername(self):
        return self.customername
    
    def validateAddress(self,address):
        #addressline,city,zipcode,state
        addressId = 0
        for a in addrlist:
            if (a.addressline == address.addressline and a.city == address.city and a.zipcode == address.zipcode and a.state == address.state):
                addressId = 0
                #pass
        
        addressId = address.addressid
        return addressId
        
    

class RegularCustomer(Customer):
    def __init__(self,customername,telephonenumber,address,discount):        
        Customer.__init__(self,customername,telephonenumber,address)
        self.discount = discount
        
class PrivilegedCustomer(Customer):
    def __init__(self,customername,telephonenumber,address,memcardtype):        
        Customer.__init__(self,customername,telephonenumber,address)
        self.memcardtype = memcardtype

        



'''
          
zipcode = '560076'
raghuaddress = Address('1094,Indushankara,23 Cross,MCECHS,Dr.Shivarama Karanth Nagar','Bengaluru',zipcode,'Karnataka')
print('address id ',raghuaddress.addressid)
print ('address line',raghuaddress.getaddressline())
isValidzipcode = raghuaddress.validatezipcode(zipcode)
if (isValidzipcode):
    print(zipcode , ' - its a valid zip code')
else:
    print(zipcode , ' - its not a valid zip code')
    
raghucust = RegularCustomer('raghu prasad',9845547471,raghuaddress,15.0)
print('customer id ', raghucust.getcustomerid())

'''
custlist = []
while (True):
    print('**** Easy Shop Retail Application****' )
    
    choice = int(input ("Enter operation you want to perform 1- Add, 2 - Modify,3-View All customers,6 - Exit"))
    if (choice == 6):
        break
    
    if (choice == 1):
        name = input("enter your name")
        tele = int(input ("enter telephone number"))
        custtype = input ("Enter customer type")
        if (custtype == 'R'):
            diccount = float(input("enter discount in percentage"))
        if (custtype == 'P'):
            cardtype = input("Enter card type")        
        
        addressline = input("Enter address line")        
        city= input("Enter city")        
        zipcode = input(input ("enter zipcode"))
        state = input ("enter state")
        #addressline,city,zipcode,state
        addr = Address(addressline,city,zipcode,state)
        #customername,telephonenumber,address,discount
        if (custtype == 'R'):
             regcust = RegularCustomer(name,tele,addr,diccount)
             custlist.append(regcust)
        if (custtype == 'P'):
            prvcust = PrivilegedCustomer(name,tele,addr,cardtype)
            custlist.append(prvcust)
    if (choice == 3):
        for c in custlist:
            
            #print('instance ' ,isinstance(c,RegularCustomer) )
            #customername,telephonenumber,address
            print (" Name : {} , telephone number : {} , Address-- city : {}, zipcode : {}".format(c.customername,c.telephonenumber,c.address.city,c.address.zipcode))
            
    if (choice == 4):
        for c in custlist:
            
            print('instance ' ,isinstance(c,RegularCustomer) )
            if (isinstance(c,RegularCustomer)):
            #customername,telephonenumber,address
                print (" Name : {} , telephone number : {} , Address : {}".format(c.customername,c.telephonenumber,c.address))
                
    if (choice == 5):
        for c in custlist:
            
            print('instance ' ,isinstance(c,PrivilegedCustomer) )
            if (isinstance(c,PrivilegedCustomer)):
            #customername,telephonenumber,address
                print (" Name : {} , telephone number : {} , Address : {}".format(c.customername,c.telephonenumber,c.address))
                
    if (choice == 2):
        echoice = input('To Modify - a - Customer Name , b - customer contact')
        if (echoice == 'a'):
            oname= input('Enter original and new name ')
            nname= input('Enter new name ')
            for c in custlist:
                if(c.customername == oname):
                    #c.customername = nname
                    c.setcustomername(nname)
            
            for c in custlist:
                print (c.getcustomername())
                
        if (echoice == 'c'):
            oname= input('Enter customer name ')
            ncity= input('Enter new city ')
            nzipcode= input('Enter new zip code ')
            for c in custlist:
                if(c.customername == oname):
                    #c.customername = nname
                    c.address.city = ncity
                    c.address.zipcode = nzipcode
                    