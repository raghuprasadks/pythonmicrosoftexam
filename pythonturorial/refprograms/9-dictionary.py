#Dictionary
tele ={'raghu':9845547471,'rakesh':9898989898,'govind':8787676765}
print(tele['rakesh'])
tele ={'raghu':9845547471,'rakesh':9898989898,'govind':8787676765,'raghu':9845547472}
print(tele['raghu'])
#copying
duptele = tele.copy()
print(duptele)
#Update
tele.update({'rakesh':8888888888})
print(tele)
tele.update({'raghu':9888888888})
print(tele)
#Delete key
del tele ['rakesh']
print(tele)
# keys
print("keys ", tele.keys())
keys = tele.keys()
for k in keys:
    print(k)
    print(type(k))
type(keys)
#values 
print("Values ", tele.values())
values = tele.values()
for v in values:
    print(v)
    print (type(v))    
#items
print("items %s :",tele.items())
for k,v in tele.items():
    print (k,v)
    print ('keys data type ',type(k))
    print ('values data type ',type(v))

#check for existance of keys
Common = {'guru': 18,'gowri':22,'Rakesh':25}
Boys = {'guru': 18,'harsha':12,'Rakesh':25}
Girls = {'gowri':22,'deepa':21}

for key in Boys.keys():
    if key in Common.keys():
        print(True)
    else:
        print(False)

#Built in function
#len
Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
print(" %d elements are in dictionary " % len (Dict))
print("Length : ",len (Dict))
#print(len(Dict), "elements are in dictionary")
#variable type
Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
print("variable Type: %s" %type (Dict))
Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
print("printable string:%s" % str (Dict))
# empty dictionary
my_dict = {}
#my_dict = {'raghu':393939,'vidya':393939}
# {'Raghu': 8383838838, 'Raghavendra': 9383838838}
my_dict['Raghu'] = 8383838838
my_dict['Raghavendra'] = 9383838838
print('new dictionary is ',my_dict)
# dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}
# dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}

# using dict()
my_dict = dict({1:'apple', 2:'ball'})
print('dict ',my_dict)
# from sequence having each item as a pair
my_dict1 = dict([(1,'apple'), (2,'ball')])
print('dict:sequence ',my_dict1)

l1 = [(1,"red"),(2,"green"),(3,"blue")]
type(l1)

l2 = [[1,"red"],[2,"green"]]

my_dict2 = dict(l2)
str(my_dict2)

for k,v in my_dict2.items():
    print (k,v)

l3 = [[1,["col1","col2"]],[2,"green"]]

my_dict3 = dict(l3)

for k,v in my_dict3.items():
    print (k,v)

#Accessing elements
my_dict = {'name':'Jack', 'age': 26}
# Output: Jack
print(my_dict['name1'])
# Output: 26
print(my_dict.get('age1'))
# Trying to access keys which doesn't exist throws error
my_dict['name1']
#does not throw error
my_dict.get('age1')

#How to change or add element to dictionary
my_dict = {'name':'Jack', 'age': 26}
# update value
my_dict['age'] = 27
#Output: {'age': 27, 'name': 'Jack'}
print(my_dict)
# add item
my_dict['address'] = 'Downtown' 
# Output: {'address': 'Downtown', 'age': 27, 'name': 'Jack'}
print(my_dict)
# Remove or delete elements
# create a dictionary
squares = {1:1, 2:4, 3:9, 4:16, 5:25} 
# remove a particular item
print(squares.pop(4))  
# Output: 16
print(squares)
# Output: {1: 1, 2: 4, 3: 9, 5: 25}
print(squares.pop(1))  
# remove an arbitrary item
# Output: (1, 1)
print(squares.popitem())
# Output: (5, 25)
print(squares)
# Output: {2: 4, 3: 9}
# delete a particular item
del squares[5]  
# Output: {2: 4, 3: 9}
print(squares)
# remove all items
print(squares.clear())
# Output: {}
print(squares)
# delete the dictionary itself
del squares
# Throws Error
#print(squares)
marks= {}.fromkeys(['Math','English','Science'], 100)
print(marks)
#{'Math': 100, 'English': 100, 'Science': 100}
for item in marks.items():
    print(item)
# Output: ['English', 'Math', 'Science']
print(sorted(marks.keys()))
lstsort = sorted(marks.keys())
print(type(lstsort))
lstnew = list(sorted(marks.keys()))
print('new lstnew ',lstnew)
#Python Dictionary Comprehension
#Dictionary comprehension is an elegant and concise 
#way to create new dictionary from an iterable in Python.
#Dictionary comprehension consists of an expression pair (key: value) followed by for statement inside curly braces {}.
#Here is an example to make a dictionary with 
#each item being a pair of a number and its square.
squares = {x: x*x for x in range(6)}
# Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(squares)
#This code is equivalent to
squares = {}
for x in range(6):
   squares[x] = x*x
print(squares)

#Dictionary Membership Test
squares= {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
# Output: True
print(7 in squares)
# Output: True
print(2 not in squares)
# membership tests for key only not value
# Output: False
print(49 in squares)
#Iterating Through a Dictionary
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
for i in squares:
    print(i)
print(len(squares))
# Output: 5
# Output: [1, 3, 5, 7, 9]
print(sorted(squares))
#pring key and ntivalues
for k, v in squares.items():
    print(k, v)
# Dynamically creating a dictionary
myfamily = {}
myfamily['raghu'] = 9845547471
myfamily['vidya'] = 9008663619
print(myfamily)
#name = 'satvik'
#phone = 8888888888
name = input("enter the name ")
phone = int(input("enter the mobile"))
myfamily[name] = phone
print(myfamily)

marks = {'raghu':88,'ravi':78,'rakesh':98}
print(max(marks.values()))
print(min(marks.values()))


#  Create following dictionary from the scratch
'''
{ "name":"raghu","city":"Bengaluru",
"address":"{"homeaddress":"1094,23 Cross,MCECHS,Jakkur",
	   "officeadress":"Kaushalya,C Block,Sahakara Nagara"}}
'''

address = {}
address["name"]="raghu"
address["city"]="Bengaluru"
addressDetails = {}
addressDetails["homeaddress"]= "1094,23 Cross,MCECHS,Jakkur"
addressDetails["officeadress"]= "Kaushalya,C Block,Sahakara Nagara"
address["address"]=addressDetails

print(address)
'''
C. Create a phone dictionary of at least 5 of your friends from the 
scratch. Add two of your new friends. Delete one old friend.
Get user inputs
'''

phonedict = {}
for i in range (5):
  name = input("Enter Name")
  mobile = input("Enter mobile")
  phonedict[name] = mobile
print("Contact details of my five friends",phonedict)
while(True):
    choice = input ("Do you want to add some more friends")
    if (choice =="Yes"):
        name = input("Enter Name")
        mobile = input("Enter mobile")
        phonedict[name] = mobile
    else:
        break
delfriend = input ("Enter the name of your friend for deletion")
for key,value in phonedict.items():
    if (delfriend ) == key:
        del phonedict[key] 
        print('Deleted ' , key)
print('latest phone list',phonedict)
