"""
Topic :- Inheritance 

Inheritance - When one clas(Child/derived) Derives the properties & Methods of another Class(Parent/base)

Types :-
Single Inheritance
Multi-level Inheritance
Multiple Inheritance
"""
# 1.Single Inheritance

class Car:
        # Parent
    @staticmethod
    def Start():
        print("Car Started...")
    
    @staticmethod
    def Stop():
        print("Car Stoped...")

        # Child
class Tata(Car):
    def __init__(self, name):
        self.name = name

car1 = Tata("TataThor")
car2 = Tata("Lamborgini")

print(car1.Start())
print(car1.name)

#2. Multi-level Inheritance
# Parent
class Car:
    @staticmethod
    def Start():
        print("Car Started...")
    
    @staticmethod
    def Stop():
        print("Car Stoped...")

# Child --> (Parent)
class Tata(Car):
    def __init__(self, name):
        self.name = name

# Child
class Fortuner(Tata):
    def __init__(self, type):
        self.type =type

Car1 = Fortuner("Audi")
Car1.Start()

# 3.Multiple Inheritence
class A:
    varA = "Welcome TO Bus1"

class B:
    varB = "Welcome TO Bus2"

class C(A,B):
    varC = "Welcome TO C"

c1 = C()
print(c1.varA)
print(c1.varB)
print(c1.varC)

