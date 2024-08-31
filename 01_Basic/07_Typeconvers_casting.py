"""
Topic :- Typecoversion and Typecasting
"""

# Typeconversion - automatically
# a = 2
# b = 4.5
# sum = (a + b) # 2.0 + 4.25 =>6.25
# print(sum)

'''Typecasting : - The conversuion of one datatype into another datatype is called Typecasting   or Typeconversion
 1. Explicit conversion ,  2. Impicit conversion'''

# 1. Explicit conversion :- The conversion of one datatype into another, datatype ,done via developer or programmer's invention as per the requirement of the programmer.
a="1"
# a=1
b="3"
# b=3
# c="1.5"
print(int(a) +int(b))
# print(int(a) +float(c))

# 2. Impicit conversion:- one datatype is converted into other in by  interpreter itself(automatically),  - Python converts a smaller data type to higher datatype to prevent data loss.
c = 1.5
d = 2
print(c + d)

# eg:-
a = 2
b = 3
c = 4

k = str(a)
o = str(b)
t = str(c)
print("sum : ", k + o + t)