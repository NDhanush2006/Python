"""
Topic :- Constructor

Constructor or _ _init_ _() :- All Classes have a function called _ _ int_ _(), which is always executed when the object is being initiated

# Dunde method :-  Dunde method is a_ _init_ _() which automatically calls it
"""
# Creating Class
class Student:
    # Class attribute

    # Default Constructors
    def __init__(self):
        pass
    
    # Parameterized Constructors
    def __init__(self, name, marks):
        self.name= name
        self.mark= marks
        print("Yay !Database......")

    def welcome(self):
        print("Hello", s2.name)


# Creating Object(Instance)

s1 = Student("BenTen", 99)
print(s1.name, s1.mark)

s2 = Student("Arjun",98)
print(s2.name, s2.mark)
s2.welcome()

