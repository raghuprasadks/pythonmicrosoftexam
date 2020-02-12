
'''
https://www.tutorialsteacher.com/python/python-read-write-file


Access Modes	Description
r	Opens a file for reading only.
rb	Opens a file for reading only in binary format.
r+	Opens a file for both reading and writing.
rb+	Opens a file for both reading and writing in binary format.
w	Opens a file for writing only.
wb	Opens a file for writing only in binary format.
w+	Opens a file for both writing and reading.
wb+	Opens a file for both writing and reading in binary format.
a	Opens a file for appending.
ab	Opens a file for appending in binary format.
a+	Opens a file for both appending and reading.
ab+	Opens a file for both appending and reading in binary format.


Mode	Description
'r'	Open a file for reading. (default)
'w'	Open a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
'x'	Open a file for exclusive creation. If the file already exists, the operation fails.
'a'	Open for appending at the end of the file without truncating it. Creates a new file if it does not exist.
't'	Open in text mode. (default)
'b'	Open in binary mode.
'+'	Open a file for updating (reading and writing)
'''


#Writing to a File

f=open("myfiledemo.txt","w")
f.write("Hello!! Learn Python from Kaushalya.tech.Python is fun to code")
f.close()


lines=["Hello world.\n", "Welcome to TutorialsTeacher.\n"]
f=open("myfiledemo.txt","w")
f.writelines(lines)
f.close()


#Open a file in append mode.
f= open("myfiledemo.txt","a")
#print(f)    
f.write('I am learning python\n')
f.write('python is easy to learn\n')
f.close()

#Reading from a File
'''
Three different methods are provided to read data from file.

readline(): reads the characters starting from the current reading position up to a newline character.
read(chars): reads the specified number of characters starting from the current position.
readlines(): reads all lines until the end of file and returns a list object.
'''

f=open("myfiledemo.txt","r")
content=f.read()
print(content)
f.close()

f=open("myfile.txt","r")
line=f.readline()
print(line)
f.close()

f=open("myfile.txt","r")
print('position before reading ',f.tell())
line=f.readline()
print('position after reading one line reading ',f.tell())
while line!='':
    print(line)    
    line=f.readline()
    print('position after reading one by one line ',f.tell())
'''
File iterator
The file object has an inbuilt iterator. The following program reads the given file line 
by line until StopIteration is raised, i.e. the end of the file is reached.
'''


f=open("D:\myfile.txt","r")
while True:
        try:
            line=next(f)
            print (line)
        except StopIteration:
            break
f.close()

# using for loop
f=open("myfile.txt","r")
for line in f:
    print(line)
f.close()


#Append and Read a File

f=open("myfile.txt","a+")
f.write("Hello! Learn Python on TutorialsTeacher.")
line=f.readline()
print(line)
f.close()


#seek() method

'''
To read or write at a specific position, use the seek() function to set the 
current read/write position.

f.seek(offset, from)

Here, the from parameter takes the following values:

0 : offset calculated from the beginning
1 : offset calculated from the current position
2 : offset calculated from the end



file.tell() - Returns the file's current position
'''

f=open("myfiledemo.txt","r+")
f.seek(6,0)
currposition = f.tell()
print('current position',currposition)
lines=f.readlines()
for line in lines:
    print(line)
    print('postion after every line',f.tell())
    
f.close()

f=open("D:\myfile.txt","r+")
f.seek(6,0)
content=f.read()
print(content)
f.close()


#Write to a Binary File
f=open("binfile.bin","wb")
num=[5, 10, 15, 20, 25]
arr=bytearray(num)
f.write(arr)
f.close()

#Reading a Binary File

f=open("binfile.bin","rb")
num=list(f.read())
print (num)
f.close()


f=open("binfile1.bin","w+b")
num=['r', 'a']
arr=bytearray(str(num),'utf-8')
f.write(arr)
f.seek(0,0)
print((f.read().decode()))
f.close()
  


#Sum of numbers in a file
f= open("samplefile.txt","r")    
lines = f.readlines()
tokens = ''
sum = 0
for l in lines:
    tokens = l.split()
    for token in tokens:
        if (token.isnumeric()):
            sum = sum + int(token)
            print(token) 
print('sum : ',sum)
f.close()

#with open

with open('hello.txt','w') as f:
    f.write('Hello World') 

with open('hello.txt','r') as f:
    data = f.readline()
    print(data)
    
'''
1. In a small firm employee numbers are given in serial numerical order 
that is 1, 2, 3, etc. Create a file of employee data with following 
information: employee number, name, sex, gross salary. 
If more employees join, append their data to the file. 
If an employee with serial number 25 (say) leaves, 
delete the record by making gross salary 0. If some employee’s gross 
salary increases, retrieve the record and update the salary. 
Write a program to implement the above operations. 
'''

f = open("employee.txt","a")
eno = "2 \t"
name = 'satvik \t'
sex = 'M \t'
gsalary = str(19900.00)
#data = eno\t name\t sex\t gsalary
f.write(eno)
f.write (name)
f.write(sex)
f.write(gsalary)
f.write("\r")

f.close()
emplist = []
nemployees = int(input("Enter number of employees "))
for i in range (nemployees):
    edata = input ('Enter details of employee using comma seperator.')
    emplist.append(edata)

f = open("employee.txt","w")
for data in emplist:
    f.write('%s\n' %data)
f.close()
f = open("employee.txt","r+")
empcode = input("enter employee code to update")
newemplist = []
for data in f:
    ecode, name,sex,gsalary = data.split(',')
    print(ecode,gsalary)
    if (empcode == ecode):
        print('matched empcode ',empcode)
        gsalary = 0    
    newdata = '{},{},{},{}'.format(ecode,name,sex,gsalary)
    newemplist.append(newdata)    
f.close()

f = open("employee.txt","w")
for data in newemplist:
    f.write('%s\n' %data)
f.close()




'''
l = f.readline()
while (l!=''):
    print(type(l))
    ecode, name,sex,gsalary = l.split(',')
    print(ecode,gsalary)
    if (empcode == ecode):
        print('matched empcode ',empcode)
        gsalary = 0
        updstr=''
        updstr = ecode+','+name+','+sex+','+str(gsalary)
        f.write(updstr)
    
    l= f.readline()
f.close()
'''    




#data = eno\t name\t sex\t gsalary

'''
f = open("employee.txt","w")
for li in emplist:
    f.write('%s\n' %li)
f.close()
'''

