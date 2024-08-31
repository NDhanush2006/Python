# Question1 - Create a Class 2D vector and use it to crreate another class representing 3D vector

'''
class TwoDvector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The Vector is {self.i}i + {self.j}j")

class ThreeDvector(TwoDvector):
    def __init__(self, i, j, k):
        super().__init__(i,j)
        self.k = k

    def show(self):
        print(f"The Vector is {self.i}i + {self.j}j + {self.k}k")


v = TwoDvector(1,2)
v.show()
e = ThreeDvector(1 ,3, 2)
e.show()'''

# Question2. Ceate a class 'Pets' from a class 'Animals' and further create a class 'Dog' from 'pets' Add a method 'bark' to class 'Dog'

'''
class Animals:
    pass

class Pets(Animals):
    pass

class Dogs(Pets):
    @staticmethod
    def bark():
        print("Bow Bow ......")
  
a = Dogs()
a.bark()
'''

# Question3 - Create a class 'Employee' and  add salary and increment prorpertys to it. Write a method 'salaryafterincrement' method with a @property decorator with a setter which changes the value of increment based on the salary
'''
class Employee:
    salary = 234
    increment = 20

    @property
    def Salaryafterincrement(self):
        return (self.salary + self.salary * (self.increment/100))

    @Salaryafterincrement.setter
    def Salaryafterincrement(self, salary):
        self.increment = ((salary / self.salary) -1) * 100

e = Employee()
print(e.Salaryafterincrement)
e.Salaryafterincrement = 280.8
print(e.increment)
'''



# Question4.
class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, c2):
        return Complex(self.r + c2.r, self.i + c2.i)
    
    def __str__(self):
        return f"{self.r} + {self.i}i"
        

c1 = Complex(1,1)
c2 = Complex(1,5)
print(c1 + c2)