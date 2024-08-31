# Q.Take positive integer input and tell if it is divisible by 5 or 3 but not divisible by 15.

num = int(input("Enter positive integer : "))

# Checking whether it is divisible by 15
if num % 15 == 0:
    print("The number is divisible by 15")

else:
    # Checking if divisible by 3 or 5
    if num % 3 ==0 or num % 5 == 0:
        print("number is not divisible by 15 but divisible by both 3 and 5")

    else:
        print("Number Neither divisible by 3 nor by 5")
