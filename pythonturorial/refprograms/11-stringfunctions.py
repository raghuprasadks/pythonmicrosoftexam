#Slicing index and range
var1 = 'kaushalya'
var2 = 'learning python'
print('0 th element of var1 : ',var1[0])
print('Slicing :',var2[0:8])
print(var2[:10])
print(var2[::2])
print(var2[::])
print('with offset 1')
print(var2[::1])
#length
print(len(var2))
#in - membership
print ("p" in var2)
print ("x" in var2)
#not in
print ("x" not in var2)
#Formatting -
name = 'guru'
number1 = 99
number2 = 99.556
print("name",name,"age is ",number1)
print("name is %s age is %d. Amount is %10.2f" %(name,number1,number2))
#Concatenate
name = 'guru'
number = 99
print(name+number)
print(name+str(number))
#Repeat-
name = "test"
print (name*3)
#Replace
oldstring = 'I like python'
newstring = oldstring.replace('like','love')
print('Replace :',newstring)
print ('old string ',oldstring)
print ('old string 1 ',oldstring)
oldstring = oldstring.replace('like','love')
#Upper and Lower case
convertlower = 'This Is for LOWER'
print(newstring.upper())
print(convertlower.lower())
#capitalize
name = 'delhi is capital of india'
print('capitalize ', name.capitalize())
#Join
print(":".join("Python"))
print(",".join("Python"))
newstr = ",".join("Python")
print(type(newstr))

revs = reversed(oldstring)
print(revs)
#Reverse
print('reverse ')
print(''.join(reversed(oldstring)))
#Split
word="Kaushalya Technical Training"
wordlist = word.split(' ') 
print(wordlist)
word="Kaushalya Technical Training"
print(word.split('a'))
#Immutable
x = "Kaushalya"
y=x.replace("Kaushalya","Python Training")
print(y)
print(x)
#count
count1 = x.count('a')
print('count..full length ',count1)
count1 = x.count('a',0,len(x)-2)
print('count ',count1)
test = '123'
test.isdigit()
test.isalpha()
test.isdecimal()
"Hello This".istitle()
"hello".ljust(10,"*")
"hello".rjust(10,"*")
" hello world  ".lstrip()
" hello world  ".strip()
" hello world  ".rstrip()
" hello world  ".strip("o ")
" hello world  ".strip("hed ")

'www.example.com'.strip('ecmowz.')

'Hello'.swapcase()

"they're bill's friends from the UK".title()


# Find sum of numbers in the following sentances.

sentence = "India got independance in 1947 .It become republic in 1956 "
tokensList = sentence.split(" ")
print(tokensList)

sum = 0
for t in tokensList:    
    if (t.isnumeric()):
        sum = sum + int(t)
print ('sum is ', sum)
    
# Counting number of occurance

sentence = "This is for testing occurance of words.This is for testing"
tokenList = sentence.split(" ")

for t in tokenList:
    countTracker = tokenList.count(t)
    print (t,countTracker)
    
    
# password validation
password = input('Enter password')
length = len(password)
clowercase =0
cuppercase = 0
cNumber = 0
cSplChar = 0
cinvalid = 0
if(length <6 or length >12):
    print('You have to enter password of minimum length 6 and maximum 12')
else:
    for p in password:
        if(p.isupper()):
            cuppercase = cuppercase + 1
        elif (p.islower()):
            clowercase = clowercase + 1
        elif (p.isdigit()):
            cNumber = cNumber + 1
        elif (p in '$' or p in '#' or p in '@'):
            cSplChar = cSplChar + 1  
        else :
            cinvalid = cinvalid + 1
            print ('This charecter is not allowed')
            break
        
if (cuppercase > 0 and clowercase >0 and cNumber >0 and cSplChar >0):
    print('You have entered valid password')
else:
    print('Password is invalid')                