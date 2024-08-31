'''
Topic : List

List :- List can be created with square bracket[] and comma
        List is a collection of Storing Data
        in List we can store multiple data
        List is a collection of Different Datatypes(int, float, string, etd)
        Indexing and Slicing Can be Done in List
        List are mutable
        We cannot find the maximum element (or)biggest number between different datatypes
        we cannot sort the list in Ascending order with different Dataype present in the list
        built in datatyype store set of data values


'''
# Creating empty or null list
l = []
print(type(l))

# Creating list
l1 = [1,2,3,4,5,6]
print(l1)

# Storing Different Datatypes in Lists
l2 = [1,2,3, 2.5, "Dhanush" , True , 4+9j ]
print(l2)

# Indexing List
l3 = ["Apple", 5, 12.2 , True ]
print(l3[0])
print(l3[-1])

# Slicing
print(l3[0:2])

# Reversing list
print(l3[::-1])

# Assigning and removing element
l3[0] = 100
print(l3)

'''
# Ques 1.write a Python program to store five fruits in a list entered by the user
fruits = []
f1 = input("Enter fruit 1 : ")
fruits.append(f1)
f2 = input("Enter fruit 2 : ")
fruits.append(f2)
f3 = input("Enter fruit 3 : ")
fruits.append(f3)
f4 = input("Enter fruit 4 : ")
fruits.append(f4)
f5 = input("Enter fruit 5 : ")
fruits.append(f5)
print(fruits)
'''

# Ques 2 : Write a Five Student mark via input and Display them in Ascending order in list
marks = []
f1 = int(input("Enter Mark : "))
marks.append(f1)
f2 = int(input("Enter Mark : "))
marks.append(f2)
f3 = int(input("Enter Mark : "))
marks.append(f3)
f4 = int(input("Enter Mark : "))
marks.append(f4)
f5 = int(input("Enter Mark : "))
marks.append(f5)
marks.sort()
print(marks)

# Ques 3. Two find the sum of elements present in the list
s = [1,2,3,4,5,6]
print(sum(s))