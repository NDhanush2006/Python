"""
Topic:-Multiple conditions
Multiple conditions :- Usin Logical Operators(AND, OR, NOT)
"""
#Q. Printinng Student marks of two subject  in conditional statemnt using Logical operator.

eng_marks = int(input("Enter the english Marks : "))
maths_marks = int(input("Enter the maths  Marks : "))

# if both are More than 80, print A grade
if eng_marks > 80 and maths_marks > 80:
    print("A - Grade")

# if neither of marks are more than 80 print B Grade
elif eng_marks > 80 or maths_marks > 80:
    print("B - Grade")

# if Neither of marks more than 80 
else:
    print("C - Grade")




