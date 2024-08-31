'''Q.Take input of a student and print the  grade according to marks and check the following 
    condition
    1. 81-100 very good
    2.61-80 good
    3.41-60 Average
    4.<=40 Fail
'''
marks = int(input("Enter the Marks : "))

# if marks are betwen 81-100
if marks > 80:
    print("A - Grade , very Good")

# if marks are betwen 61-80
elif marks >=60:
     print("B - Grade , Good")

#  if marks are above 40
elif marks >=41:
     print("c - Grade , Average  work hard and Keep improve")

#  if marks below 40 ,Fail
else:
     print("F - Grade , Fail Works More on subjects")
     

