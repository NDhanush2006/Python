# Take positive integer input and tell if it is Even or Odd
# Even - which divisible by 2 and remainder is Zero then it  is even number
# odd - which divisible by 3 is odd number(Hint - use Modulus operaator)

n = int(input("Enter a number : "))

if (n% 2==0):
    print("It is Even Number")

else:
    print("It is Odd Number")
