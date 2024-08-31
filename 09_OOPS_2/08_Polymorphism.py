"""
Polymorphism : Operator Overloading
When the same operator is allowed to have different meaning according to the context
"""

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    
    def calc(self):
        print(self.real,"i +", self.img,"j")
c = Complex(2 , 3)
c.calc()
# print(c.real, c.img)