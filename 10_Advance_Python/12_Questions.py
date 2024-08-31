# Question1. Write a python program to open three files 1.txt, 2.txt, 3.txt. if any these files aremnot present, a message without existing the program must be printed prompting the same.
'''
# Question2. Write a program to print third, fifth and seventh element from a list using enumerate function

try:
    with open("1.txt", "r") as f:
        print(f.read())

except Exception as e:
    print(e)

try:
    with open("2.txt", "r") as f:
        print(f.read())

except Exception as e:
    print(e)

try:
    with open("3.txt", "r") as f:
        print(f.read())

except Exception as e:
    print(e)

print("The File Doesn't exist")
'''
# Question2. Write a program to print third, fifth and seventh element from a list using enumerate function
'''
l = [ 2 , 4, 6, 8, 10, 15, 23, 50]

for i, item in enumerate(l):
    if(i == 3 or i == 5 or i == 7):
        print(f" {item}")'''

# Question3 . Print multiplication table of n natural number using List Comphrension
# n = int(input("Enter n Number : "))
# table = [n*i for i in range(1, 11)]
# print(table)

# Question4. Write a program to display a/b where a and b are integers . if b = 0,display infinite by handling the "ZeroDivision error"
'''
try:
    a = int(input("Enter n number : "))
    b = int(input("Enter n number : "))
    print(a/b)

except ZeroDivisionError as e:
    print("Error Occured is : ",e)'''

# Question5. 
n = int(input("Enter n Number : "))
table = [n*i for i in range(1, 11)]
with open("table.txt", "a") as f:
    f.write(f"Table of {n} : {str(table)}  \n")