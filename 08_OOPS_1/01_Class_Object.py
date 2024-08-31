'''
Topic :-(OOPS - Object oriented programing) - To map with real world scenario, we started using code
Class & Object in python-
Class : Class is a Blueprint for creating objects
Object: Things

'''
#Creating Class(Noun)
class Car:
    #Class Attributes
    no_of_wheels = 4
    mileage = 29.4
    no_of_airbags = 2

    def moveForward(self):
        print("Car is Moving")

    def moveBackward(self):
        print("Car is Moving Backward")

# Creating Object(Instance)
# ObjectAttribute
# method
car1= Car() #instance of a Class
print(car1.mileage)
print(car1.no_of_airbags)

car2 = Car()
# Changing Value
car2.mileage = 100
print(car2.mileage)
print(car2.no_of_airbags)

car3 = Car()
car3.moveForward()
