
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

f=open("D:\myfile.txt","w")
f.write("Hello! Learn Python from Kaushalya.tech.")
f.close()


lines=["Hello world.\n", "Welcome to TutorialsTeacher.\n"]
f=open("D:\myfile.txt","w")
f.writelines(lines)
f.close()


#Open a file in append mode.
f= open("filedemo13112019demo.txt","a")
print(f)    
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

f=open("D:\myfile.txt","r")
line=f.readline()
print(line)
f.close()


f=open("D:\myfile.txt","r")
line=f.readline()
while line!='':
    print(line)
    line=f.readline()
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
f=open("D:\myfile.txt","r")
for line in f:
    print(line)
f.close()


#Append and Read a File

f=open("D:\myfile.txt","a+")
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

f=open("D:\myfile.txt","r+")
f.seek(6,0)
currposition = f.tell()
print('current position',currposition)
lines=f.readlines()
for line in lines:
    print(line)
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











