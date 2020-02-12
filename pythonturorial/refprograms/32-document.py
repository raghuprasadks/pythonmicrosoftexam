#https://realpython.com/documenting-python-code/
def sayHello():
    """
    This is a simple Hello function
    """
    print("Hello")
    
def timePass():
    """
    I do not do any thing..
    """
    pass

sayHello()

print("document :", sayHello.__doc__)
help(sayHello)
help("for")

timePass()