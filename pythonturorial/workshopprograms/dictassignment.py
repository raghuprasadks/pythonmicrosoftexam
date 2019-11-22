tele = {}

def AddFriend(name,number):
    tele[name] = number

def SearchForFriend(name):
    if name in tele.keys():
        return True
    else:
        return False


def DeleteFriend(name):
    print(name, " with ",tele.pop(name), " numbers is deleted from directory")

while(True):
    choice = int(input("Select Your Choice:\n1.Add Friend In Dictionary\n2.Search for Friend\n3.Update Phone of Friend\n4.Delete a Friend\n5.Exit\nChoice:"))
    if(choice == 1):
        name = input("Enter Name of Friend:")
        number = input("Enter Number of %s :"%(name))
        AddFriend(name,number)
    elif(choice==2):
        name = input("Enter Name you want to search:")
        if SearchForFriend(name):
            print("Number of ",name, " is ",tele[name])
        else:
            print(name, " does not exist in directory")
    elif choice==3:
        name = input("Enter Name you want to search:")
        if SearchForFriend(name):
            number = input("Enter new Number:")
            AddFriend(name,number)
        else:
            print(name, " does not exist in directory")
    elif choice==4:
        name = input("Enter Name you want to search:")
        if SearchForFriend(name):
            DeleteFriend(name)
        else:
            print(name, " does not exist in directory")
    elif choice==5:
        break
    else:
        print("Please Enter Choice")
    print("Current Directory:",tele)


