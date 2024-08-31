"""
#Calculating sum in Normal
Sum = 1 + 2 + 3 + 4 +.... n

#Calculating sum in Recursion
sum(1) = 1
sum(2) = 1 + 2 
sum(3) = 1 + 2 + 3 
sum(4) = 1 + 2 + 3 + 4 
sum(5) = 1 + 2 + 3 + 4 + 5

Sum = 1 + 2 + 3 + 4 +.... n-1 + n
sum(n) = sum(n-1) + n

# Question. write a recursive function to calculate sum of firsst n natural number.
"""

def sum(n):
    if(n == 0):
        return 1
    else:
        return sum(n-1) + n

print(sum(5))

# Question2. write a recursion function to print all elements in a list

# def list(list, index = 0):
#     if( index == len(list)):
#         return
#     print(list[index])
#     list(list, index+1)

# l = ["a", "b", "c", "d", "e"]

# list(l)