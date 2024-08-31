"""
Topic :- Operators

Operators :-An operator is a symbol that performs a certain operation between operands.
a, b, c -operands
+, -, *, /- operators
1.Arithmetic operators           6.Comparison operator
2.Assignment operators           7.Membership operator
3.Relational operator            8.Identity operator
4.Logical operators
5.Bitwise Operators
"""
'''
# 1.Arithmetic Operators.
# Operator             Name            Exaple
    +               Addition            x+y 
    -               Subtraction         x-y
    *               Multiplication      x*y
    /               Division            x/y
    %               Modulus             x%y
    **              Exponential         x**y
    //              Floor Division      x//y
'''
'''
a = 10
b = 2

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
print(a//b)
'''
# Relational operators/Comparison operator:- if the given condition is satisfy it will write false , else it will write false(==, !=, >, <, >=, <=)
"""
a = 50
b = 20

print(a == b) #false
print(a != b) #True
print(a >= b) #true
print(a > b) #true
print(a <= b) #false
print(a < b) #false
"""

# Assignment operators(=, ==, !=, +=, -=, *=, /=, **=, //=)
# n = 10
# n = n + 10
# print("num : ", n)

m = 10
m+=10
print("num : ", m)
x = 10
x -=10
print("num : ", x)

# Logical Operator -(not, and, or)
a = 50
b = 20
# print(not False)

var1 = True
var2 = True
print( a==b and a > b)

print( a==b or a > b)
print(  not a > b)

# Identity operator((is) -returns true if both the variables are same object,( is not) -returns true if both the variables are not same object)
x =5
y =5
print("if x is y : ",x is y)
print("if x is not  y : ",x is not y)

# Membership operator(in , not in)
fru =["apple","banana","cherry"]
print("if banana is present in fruits : ", "banana" in fru)
print("if apple is not present in fruits : ", "mango" not in fru)

# Bitwise operator(&, ^, ~, <<, >>, |)
a = 5
b = 3

print(" a not b : ", a & b)
print(" a XOR b : ", a ^ b)
print(" a OR  b : ", a | b)

# Operator precedence -(BODMAS - (), /, *, +, -)
'''
1.() -> 2.** -> 3. /, //, % -> 4.* -> 5. +, - -> 6.bitwise -> 7.comparisson ->8.Logical
'''
c = 3 + 2 **4/2*5-8//2
print(c)