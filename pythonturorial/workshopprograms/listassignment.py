data = [100,50,30,20,500]
sum1 = sum(data)
len1 = len(data)
avg = sum1/len1
print('Sum is ',sum1)
print('average is ',avg)
print('minimum ',min(data))
print('maximum ',max(data))
'''
without using built-in function
'''
sum = 0
max = data[0]
min = data[0]
count = 0
for n in data:
    sum = sum +  n
    if (n > max):
        max = n
    if (n < min):
        min = n
    count = count+1
avg = sum/count
print('Sum is %d' %(sum))
print('maximum is ',max)
print('minimum is ',min)
print('Average is ',avg)
print('sum = %d, max = %d,min =%d,avg=%f' %(sum,max,min,avg))
