'''
Python - Random Module
Functions in the random module depend on a pseudo-random 
number generator function random(), 
which generates a random float number between 0.0 and 1.0.

random.random(): Generates a random float number 
between 0.0 to 1.0. The function doesn't need any arguments.

'''

import random
r = random.random()
print('random float ',r)

'''
random.randint(): Returns a random integer between the 
specified integers.
'''
i = random.randint(1,100)
print('random int ',i)

'''
random.randrange(): Returns a randomly selected element 
from the range created by the start, stop and step 
arguments. The value of start is 0 by default. 
Similarly, the value of step is 1 by default.
'''
random.randrange(1,10)

random.randrange(1,10,2)

'''
random.choice(): Returns a randomly selected element 
from a non-empty sequence. 
An empty sequence as argument raises an IndexError.
'''
random.choice('computer')
random.choice([12,23,45,67,65,43])

random.choice((12,23,45,67,65,43))
'''
random.shuffle(): This functions randomly reorders the 
elements in a list.
'''
numbers=[12,23,45,67,65,43]
random.shuffle(numbers)
numbers
