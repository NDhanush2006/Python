try:
    a = int(input("Enter a number : "))
    print(a)

except Exception as i:
    print(i)

finally:
    print("Yay!...")