# If try was Successfuly run then it prints the else part

try:
    a = int(input("Enter a number : "))
    print(a)

except Exception as i:
    print(i)

else:
    print("Yay!...")