"""
Super method() - Super() method is used to access methods of tthe parent class
"""

class Car:
    def __init__(self, type) :
        super().__init__(type)
        self.type = type
        
        # Parent
    @staticmethod
    def Start():
        print("Car Started...")
    
    @staticmethod
    def Stop():
        print("Car Stoped...")

        # Child
class Tata(Car):
    def __init__(self, name, type):
        self.name = name
        self.type = type
        super().Start()
        

Car1 = Tata("Lambo","Fuel")
print(Car1.type)