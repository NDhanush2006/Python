"""
Abstraction :- Hiding the implementation details of a class and only ahowing essential features of the user

Encapsulation : Wrapping data and function into a single unit(object)
"""

# Abstraction
class car:
    def __init__(self):
        self.acc = "HI"
        self.brk = "Ok"
        self.clutch = "Done"

    def start(self):
        self.acc = "HI"
        self.brk = "Ok"
        print("Car Started.....")

car1 = car()
car1.start()
