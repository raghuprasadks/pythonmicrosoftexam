#Tuple
#https://www.programiz.com/python-programming/tuple
#https://www.geeksforgeeks.org/tuples-in-python/
months =('Jan','Feb','Mar','Apr')
print("Tuple months :",months)
numbers =(1,2,3,4,5,6)
print("Tuple numbers :",numbers)
print("Slicing : ",months[0:2])
# empty tuple
# Output: ()
my_tuple = ()
print(my_tuple)
# tuple having integers
# Output: (1, 2, 3)
my_tuple = (1, 2, 3)
print(my_tuple)
# tuple with mixed datatypes
# Output: (1, "Hello", 3.4)
my_tuple = (1, "Hello", 3.4)
print(my_tuple)
# nested tuple
# Output: ("mouse", [8, 4, 6], (1, 2, 3))
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)

#my_tuple.append(45)
lst = my_tuple[1]
lst.append(15)
print(my_tuple)


# tuple can be created without parentheses
# also called tuple packing
# Output: 3, 4.6, "dog"

my_tuple = 3, 4.6, "dog"
print(my_tuple)
print(type(my_tuple))
# tuple unpacking is also possible
# Output:
# 3
# 4.6
# dog
a, b, c = my_tuple
print(a)
print(b)
print(c)
#Packinng
personalinfo = ('Raghu','Kayshalya.tech','Bengaluru')
#unpacking
(Name,Company,City) =personalinfo
print (Name)
print (Company)
print (City)
#Comparision
a=(10,12)
b= (7,9)
if(a>b):
    print("A is bigger")
else:
    print("B is bigger")

a=(5,6)
b=(5,4)
if (a>b):
    print("a is bigger")
else:
    print("b is bigger")

a=(5,6)
b=(6,4)
if (a>b):
    print("a is bigger")
else:
    print("b is bigger")

a=(5,5)
b=(5,5)
if (a>b):
    print("a is bigger")
elif (b==a):
    print('a is equal to b')
else:
    print("b is bigger")

#Tuples and dictionary

a={'X':100,'Y':200}
b=a.items()
print(b)
print(type(b))
#dict_items
#dict_items([('X', 100), ('Y', 200)])

#Deleting tuple
c=(100,101)
del c

tup = (100,344,885)

newlst = list(tup)
print(newlst)

#print(c)
#Max and min
numberst = (10,5,200,7,1,300)
print(max(numberst))
print(min(numberst))
print(sorted(numberst))
print(sorted(numberst,reverse=True))
print(len(numberst))


#REVA Questions
tuple1 = (10,"Hello",10.5,10+5j,'a',"Hello",10)
#valid functions
tuple1.index(10.5)
tuple1.count("Hello")

#invalid functions
tuple1.append(10)
tuple1.pop()
tuple1.insert(3,10)





