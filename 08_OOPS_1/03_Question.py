# Question1 

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def getavg(self):
        sum =0
        for val in self.marks:
            sum+= val
        print("Yay ",self.name ,"The Average of three number is : ", sum/3)



s1 = Student("Arjun", [90,99,89])
# Changing Name
s1.name = "Ironman"
# print(s1.name, s1.marks)
s1.getavg()
        