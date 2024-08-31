'''
Static method : Methods that don't use the self parameter(work at class level)
'''

class Student:

    @staticmethod #Decorator
    def  college():
        print("ABC College")

s1= Student()
s1.college()
