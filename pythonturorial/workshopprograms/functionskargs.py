'''
def multiargs(* args):
    print(type(args))
    print(args)

multiargs('Hello')
multiargs('hello','python')
multiargs(1,2,3)
'''
def defaultValue(name,univ='REVA',place='Bengaluru',pincode=None):
    print(name,univ,place,pincode)


defaultValue('Ravi')
defaultValue('Samhita',pincode=560064)
