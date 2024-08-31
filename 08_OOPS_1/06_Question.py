# Question1. Create a class "Programmer" for storing information of few programmers working at microsoft

# class Programmer:
#     Company = "Microsoft"

#     def __init__(self,name,salary,pin):
#         self.name = name
#         self.salary = salary
#         self.pin = pin

# p= Programmer("Karan", 150000, 123456)
# print(p.name,p.salary, p.pin)
# r= Programmer("Virat", 150000000, 123456)
# print(r.name,r.salary, r.pin)

# Question2 Write a class "Calculator" capable of finding Square, cube and square root of a Number

class Calculator:
    def __init__(self,n):
        self.n = n
    def square(self):
        print(f"The square is : {self.n*self.n}")

    def cube(self):
        print(f"The square is : {self.n*self.n*self.n}")

    def squareroot(self):
        print(f"The square is : {self.n**1/2}")

a = Calculator(4)
a.square()
a.cube()
a.squareroot()

# Question3. Create a class with a class attribute a; create an objecct from it and set 'a'directly using object.a = 0. Does this change the class attribute(No)

class Demo:
    a = 4

o = Demo() 
print(o.a)#Prints the class attribute because instance attribute is not present

o.a = 0 #Prints the class attribute because instance attribute is present
print(o.a)
print(Demo.a) #Prints the class  Attribute

