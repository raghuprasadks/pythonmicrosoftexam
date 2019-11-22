name = input("Enter your name")
print(type(name))
print('your name is ',name)

age = int(input("enter your age"))
print('your age is ',age)

nextyear = age +1
print('your age after one year',nextyear)

amount = float(input("Enter the payment made for purchase of fruits"))
print('float conversion',amount)

print("Enter names of your friends")
friends = eval(input("Enter names as a list"))
print('evaluated as list ',type(friends))
print('here comes your friends ',friends)
