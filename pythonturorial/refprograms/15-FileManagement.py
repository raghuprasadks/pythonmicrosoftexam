'''
Mode	Description
'r'	Open a file for reading. (default)
'w'	Open a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
'x'	Open a file for exclusive creation. If the file already exists, the operation fails.
'a'	Open for appending at the end of the file without truncating it. Creates a new file if it does not exist.
't'	Open in text mode. (default)
'b'	Open in binary mode.
'+'	Open a file for updating (reading and writing)
'''
def main():
    f= open("dhanyatest.txt","+")
    for i in range(50,61):
        f.write("This is new line %d\r\n" % (i))      
    f.close()
    #Open the file back and read the contents
    f=open("dhanyatest.txt", "+")
    if(f.mode == 'r'):
        contents =f.read()
        print(contents)
   #or, readlines reads the individual line into a list
   #fl =f.readlines()
   #for x in fl:
   #print x
    f.close()
if __name__== "__main__":
  main()
  
#Open a file in append mode.
f= open("filedemo13112019demo.txt","a")
print(f)    
f.write('I am learning python\n')
f.write('python is easy to learn\n')
f.close()
 
#file in write mode.
f= open("filedemo13112019demo.txt","w")    
f.write('I am learning python\n')
f.write('python is easy to learn\n')
f.close()

#Reading a file r mode.
f= open("filedemo13112019demo.txt","r")    
print(f.read())
f.close()

#Reading line by line
f= open("filedemo13112019demo.txt","r")    
lines = f.readlines()
for l in lines:
    print(l)
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

#https://www.tutorialsteacher.com/python/python-read-write-file
f= open("dhanyatest1.txt","a+")
f.write('testing')
f.seek(0,0)
contents =f.read()
print(contents)
print(f.mode)
f.close()

f=open("binfile.bin","w+b")
num=[5, 10, 15, 20, 25]
arr=bytearray(num)
f.write(arr)
f.seek(0,0)
print(list(f.read()))
f.close()
f=open("binfile.bin","w+b")
num=['r', 'a']
arr=bytearray(str(num),'utf-8')
f.write(arr)
f.seek(0,0)
print((f.read().decode()))
f.close()

string = "Python is interesting."
# string with encoding 'utf-8'
arr = bytearray(string, 'utf-8')
print(arr)










