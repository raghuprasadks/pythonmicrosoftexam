#https://runestone.academy/runestone/books/published/thinkcspy/SimplePythonData/OrderofOperations.html

'''
PEMDAS - parenthesis, exponents, multiplication, division, addition, subtraction

Rules of precendence 

Parentheses have the highest precedence and can be used to force an expression to evaluate in the order you want. Since expressions in parentheses are evaluated first, 2 * (3-1) is 4, and (1+1)**(5-2) is 8. You can also use parentheses to make an expression easier to read, as in (minute * 100) / 60, even though it doesn’t change the result.

Exponentiation has the next highest precedence, so 2**1+1 is 3 and not 4, and 3*1**3 is 3 and not 27. Can you explain why?

Multiplication and both division operators have the same precedence, which is higher than addition and subtraction, which also have the same precedence. So 2*3-1 yields 5 rather than 4, and 5-2*2 is 1, not 6.

Operators with the same precedence (except for **) are evaluated from left-to-right. In algebra we say they are left-associative. So in the expression 6-3+2, the subtraction happens first, yielding 3. We then add 2 to get the result 5. If the operations had been evaluated from right to left, the result would have been 6-(3+2), which is 1
An exception to the left-to-right left-associative rule is the exponentiation operator **. A useful hint is to always use parentheses to force exactly the order you want when exponentiation is involved:
'''
'''
https://www.tutorialspoint.com/python/operators_precedence_example.htm
**	Exponentiation (raise to the power)
~ + -	Complement, unary plus and minus (method names for the last two are +@ and -@)
* / % //	Multiply, divide, modulo and floor division
+ -	Addition and subtraction
>> <<	Right and left bitwise shift
&	Bitwise 'AND'td>
^ |	Bitwise exclusive `OR' and regular `OR'
<= < > >=	Comparison operators
<> == !=	Equality operators
= %= /= //= -= += *= **=	Assignment operators
is is not	Identity operators
in not in	Membership operators
not or and	Logical operators


'''
exp1 = 2*(3-1)
print(exp1)

exp2 = 2*3-1
print(exp2)

exp3 = 2*2+2**3-(4*2)
print(exp3)

print(2 ** 3 ** 2)     # the right-most ** operator gets done first!
print((2 ** 3) ** 2)   # use parentheses to force the order you want!

'''
Assignments. Find the value of following expressions

'''

16 - 2 * 5 // 3 + 1
2 ** 2 ** 3 * 3
