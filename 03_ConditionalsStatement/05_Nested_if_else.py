'''
Topic :- Nested(if-else)
'''
# Q.Find the Greatest of Three numbers

n1 = int(input("Enter A  Number : "))
n2 = int(input("Enter B  Number : "))
n3 = int(input("Enter C  Number : "))

# Using Nested if else Statement
# if n1 (or) A is Greatest
if n1 > n2:
    # either n1 or n3 is  greatest
    if n1 > n3:
        print(n1," is The greatest number")
    
    else:
        print(n3,"is The Greatest Numbers")

else:
    # either n2 or n3 is greatest
    if n2 > n3:
        print(n2,"is the Greatest number")
    
    else:
        print(n3,"is the Greatest number")
    

