# Question1. Create one Virtual environments, install few Packages in the first one.How do you create similar environment in the second one ?
''' 1. pip install virtualenv
    2.virtualenv myproject
    3.install your package
    4.Deactive First to run second Virtual Environment , same step as follow to second one
'''

# Question2. Write a program to input name, marks, and phoneno of a student usng fomat string 
'''
name = input("Enter name : ")
marks = int(input("Enter name : "))
Phoneno = int(input("Enter name : "))
a ="My name is: {}\nMark is : {}\nPhoneno :{}".format(name, marks, Phoneno)
print(a)'''

# Question3.
'''
n = int(input("Enter name : "))

table = [str(n*i) for i in range(1,11)]
s = "\n".join(table)
print(s)'''

# Question4. Write a python program to filter a list of numbers which are divisible by 5
# l = [1, 5, 18, 22, 45, 50]
# def divisible(n):
#     if n%5==0:
#         return True
#     return False

# f = filter(divisible,l)
# print(list(f))

# Question5. write a program to find the maximum number in a list using the reduce function
list = [1, 20, 8, 15, 66, 99]
from functools import reduce
def greater(a,b):
    if (a>b):
        return a
    return b
print(reduce(greater, list))