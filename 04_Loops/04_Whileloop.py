'''
Topic :- While Loop
'''
# it will print infinite loop because True
# while True:
#     print("Hello")

'''
# Iterator
count = 1
#       Iteration
while count <= 5:
    print("Hello Dhanush", count)
    count += 1
# print(count)

# printing numbers from 1 to 5
i = 1
while i <= 5:
    print(i)
    i+=1

# Reversing Loop from 5 to 1
i = 5
while i >= 1:
    print(i)
    i-=1
'''
# # Printing table of a n number 
# i = 1
# num = int(input("Enter n number : "))
# n = int(input("Enter n number : "))
# while i <= num:
#     print(i,"X",n,"=",i*n)
#     i+=1

# Print the elements of the following list using a loop
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Traverse
nums = [1, 4, 9, 12, 15, 17, 23, 34, 88, 100]
# idx = 0
# while idx < len(nums) :
#     print(nums[idx])
#     idx +=1

# Search for an nummber x in a tuple 
x = int(input("Enter x element to search : "))
i = 0
nums = (1, 4, 9, 12, 15, 17, 23, 34, 88, 100)
while i < len(nums):
    if nums[i] == x:
        print("Found at index : ", i)
    i += 1

