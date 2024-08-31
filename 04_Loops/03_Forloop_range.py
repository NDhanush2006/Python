'''
Topic :- For loop Range()

Range() - Range function Returns a sequence of numbers always start from 0 by default, and increments by 1(by default), and stops before a specified number
Range(start,stop,step)

'''
"""
# Range (stop)
for i in range(10):
    print(i)

# Range (start,stop)
for i in range(2, 10):
    print(i)

# Range(start,stop,step)
for i in range(1,10,2):
    print(i)
    """
# Printing Tables using Forlooprange

# n = int(input("Enter n : "))
# for i in range(1, 11):
#     print(n * i)

# Ques. Write a program to creat all the person name stored in a lists 'l' and which starts with S.
l = ["Harry", "sam", "sarath","ram"]
for name in l:
    if name.startswith('s'):
        print(f"Hello {name}")