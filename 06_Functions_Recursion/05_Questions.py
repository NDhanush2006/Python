'''Question1 . Write a program using functions to find greatest of three numbers'''
def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>b and b>a):
        return c
    
a = 1
b = 2
c = 3
print(greatest(a,b,c))

'''Question2 .Write a program using functions to Convert celsius to  fahrenheit
c = 5*(f-32)/9'''

def f_to_c(f):
    return 5*(f-32)/9

f = int(input("Enter temperature in fahrenheit: "))
print(f"{f_to_c(f)} degree Celsius")

'''
Question3. Write a python function to print first n lines of the following pattern
for n = 3
* * *
* *
*
'''
def pattern(n):
    if (n== 0):
        return
    else:
        print("*" * n)
        pattern(n-1)

pattern(5)

# Question 4 write a python program using Function to Converting inches to centimeter
def inch_to_cms(inch):
    return inch * 2.54

n = int(input("Enter number : "))

print(inch_to_cms(n))

# Question 5
def rem(l , word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n

l = ["Harry", "Rohan", "Shubham", "Rajan"]

print(rem(l, "an"))
