# Square root calculation
import math
print('sqrt ', math.sqrt(4))
#power
print('power ',math.pow(2,3))
#absolute value
print('absolute value', math.fabs(-10))
#Ceil
x = 16.4
print('ceil ',math.ceil(x))
#Floor
print('Floor ',math.floor(x))
#Factorial
print('Factorial ',math.factorial(4))
# Remainder
print('remainder ',math.fmod(10, 5))
#Not a number
print('Is a number ',math.isnan(10))
# pi value
print('value of pi', math.pi)

# Euler's number
print("Value of Euler's number ",math.e)

'''
The math module contains functions for calculating various trigonometric 
ratios for a given angle. The functions (sin, cos, tan, etc.) 
need the angle in radians as an argument. We, on the other hand, are 
used to express the angle in degrees. The math module presents two angle
 conversion functions: degrees() and radians(), 
to convert the angle from degrees to radians and vice versa.

'''

print('radians ',math.radians(30))
print ('degrees' ,math.degrees(math.pi/6))


'''
The following statements show sin, cos and tan ratios for the angle 
of 30 degrees (0.5235987755982988 radians):
'''

math.sin(0.5235987755982988)
math.cos(0.5235987755982988)
math.tan(0.5235987755982988)

'''
You may recall that sin(30)=0.5, cos(30)=32 (which is 0.8660254037844387) and 
tan(30)= 13 (which is 0.5773502691896257).
'''


