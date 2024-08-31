class Student:

    def __init__(self, phy, chem, maths):
        self.phy = phy
        self.chem = chem
        self.maths = maths

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.maths) / 3)  + "%"

stu1 = Student(98, 90, 97)
print(stu1.percentage)

stu1.phy = 92
print(stu1.percentage)
