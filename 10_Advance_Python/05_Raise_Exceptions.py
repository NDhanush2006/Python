a = int(input("Enter a number : "))
b = int(input("Enter b number : "))

if(b == 0):
    raise ZeroDivisionError("These Means We can not Divide numbers by Zero")

else:
    print(f"The division a/b is : {a/b}")