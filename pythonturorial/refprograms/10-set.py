# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 10:15:17 2018
@author: Raghu Prasad

https://www.programiz.com/python-programming/set
"""
#A set is a collection which is unordered and unindexed. 
#In Python sets are written with curly brackets.
#Create a Set:
thisset = {"apple", "banana", "cherry"}
#{'cherry', 'apple', 'banana'}
print(thisset)
#print(thisset[0])
#Access Items
for x in thisset:
  print(x)

#Check if "banana" is present in the set:
print("banana" in thisset)
#Change Items
#Once a set is created, you cannot change its items, but you can add new items.
#add
print(thisset)
#update
thisset.update(["orange", "mango", "grapes","banana"])
print(thisset)
#length
thisset = {"apple", "banana", "cherry"}
print(len(thisset))
#remove
thisset.remove("banana1")
print(thisset)
#Note: If the item to remove does not exist, remove() will raise an error.
thisset.discard("banana1")
print(thisset)
#Note: If the item to remove does not exist, discard() will NOT raise an error.
#pop
x = thisset.pop()
#Clear empties the set
thisset.clear()
#del deletes the set completely
del thisset
# The set() Constructor
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
newset = set(("apple","banana"))
print('newset',newset)

newset = set(("apple", ("mango","Water Melon"), "cherry")) 
# note the double round-brackets
print(newset)
for t in newset:
    print(t)
    typeof = type(t)
    print(typeof)
    if (isinstance(t, tuple)):
        print("it's a tuple")
        

def arthoperation(operator,num1, num2):
    #result = 0
    formatstr = ''
    if (operator == '+'):
        #result = num1+num2
        formatstr = "{} + {} = {} ".format(num1, num2, num1 + num2)
    elif (operator == '-'):
        formatstr = "{} - {} = {} ".format(num1, num2, num1 - num2)
    else:
        print('invalid operator ')
    
     
    return formatstr

result = arthoperation ('+',10,5)
print (result)