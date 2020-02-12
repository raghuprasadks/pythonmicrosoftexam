data = eval(input("Enter a list"))
print(data)

max = data[0]
sum = 0
noofelements = 0
search = int(input('Enter element to search'))
for i in data:
    sum = sum + i
    noofelements = noofelements +1 
    if (i >max):
        max = i
    if (i == search):
        print('Found element ' ,search,' at ',noofelements-1 )
 
print('Maximum is ',max)
print('sum is ',sum)
average = sum/noofelements
print('Average is ',average)