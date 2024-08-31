n1 = int(input("Enter A  Number : "))
n2 = int(input("Enter B  Number : "))
n3 = int(input("Enter C  Number : "))


# if n1 (or) A is Greatest
if n1 > n2 and n1> n3:
    print(n1 ,"of A is Greatest")

# if n2 (or) B is Greatest
elif n2 > n1 and n2 > n3:
    print(n2,"B is Greatest")

# if n3 (or) C is Greatest

else:
    print(n3,"C is Greatest")