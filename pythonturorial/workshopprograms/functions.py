def greet():
    print('Hello')
greet()
def greet(name):
    print('Hello. Welcome ',name)

nam= input("Enter a name")
greet(nam)

def simpleInterest(p,r,t):
    si = p*r*t/100
    return si
si = simpleInterest(1000,6,1)

print('Simple interest is ',si)
def multireturn(n1,n2):
    sum = n1 + n2
    return n1,n2,sum
n1,n2,s = multireturn(100,200)
print('sum of ',n1,' ', n2, ' is ',s)
    
