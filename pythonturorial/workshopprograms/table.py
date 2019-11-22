#num=5
'''
num = int(input("Enter a number to print the table"))
i=1
while i <= 10:
    print ( num, " X " , i , " = ", (num*i))
    i+=1

r = range (10)
print('range',r)

for n in range(11):
    print(n)

for n in range(1,11):
    print(n)

for n in range(5,51,5):
    print(n)

for n in range(50,0,-5):
    print(n)
'''
print('break')
for n in range(50,0,-5):
    if (n == 25):
        break
    print(n)
print('continue')
for n in range(50,0,-5):
    if (n == 25):
        continue
    print(n,end = ' ')
    

    
