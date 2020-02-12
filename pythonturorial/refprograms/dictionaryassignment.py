teledirectory = {}

nooffriends = int(input("Enter number of best friends"))

for i in range(nooffriends):
    name = input ("Enter friend name")
    mobile = int(input ("Enter mobile number"))
    teledirectory[name] = mobile

print('Tele directory of my best frieds',teledirectory)