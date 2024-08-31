"""
Topic :- Sets

Sets :- set is the collection of the unordered items
        Each element in the set must be unique & immutable
        it contain duplicate value,but while printing it contain(takes) unique data
        it didn't arranged in sequence, while printing it changes the position every element
        in strings it Doesn't see Duplicate value in string ,it is very case sensitive(in python)
        we cannot add list in sets  -bcoz list are mutable
        we can add tuples in sets - bcoz tuple are immutable same as set(only) immutable set can be added
        we can not add set inside set
        Indexing cannot be done bcoz, set takes randomly store unique value
        sets are unordered, indexed 
        There is no way to change the items in sets
        sets cannot contain duplicate value
"""
# Creating Set
s = set()
print(type(s))

s1 ={1,2,4,5,5,1,6,6,6,6,7,8,"apple", "Skills"}
print(s1)

s2 = {"Skills", "skills", "skills"}
print(s2)

# Set inbuilt functions
# 1.add() - it adds element in string, we can not add any element again if it is already exits in sets
s2.add("pw")
print(s2)

# 2.clear() - it remove all element in the set
s2.clear()
print(s2) 

# Converting list into set
l = [1,2,2,2,1,3,4,4,4,3,2,4,5,6,7,8,8,9,10,2,]
print(set(l))

# Converting tuple into set
t = (1,2,2,2,1,3,4,4,4,3,2,4,5,6,7,8,8,9,10,2,"ohk", "raj")
print(set(t))

# Converting list into set and again coverting set into list
l = [1,2,2,2,1,3,4,4,4,3,2,4,5,6,7,8,8,9,10,2,]
print(list(set(l)))

# Converting tuple into set and again converting set into tuple
t = (1,2,2,2,1,3,4,4,4,3,2,4,5,6,7,8,8,9,10,2,"ohk", "raj")
print(tuple(set(t)))

# 3.remove() - Remove an element from a set; it must be a member,If the element is not a member, raise a KeyError.
s1.remove("apple")
print(s1)

# 4.discard() - if the given element is not present , then it doesn't give error
s2.discard(100) #output :- None
print(s2)

# 5.pop() - it automatically picks any element in the set or orbitary
s1.pop()
print(s1)

# 6.union() -Combines both set values and return new
set1 = {1 , 2, 3}
set2 = {2 , 3, 6}
print(set1.union(set2))


# 7.intersection() - combines common values and returns new
print(set1.intersection(set2))


# Question1 write a program to input eight numbers from the user and display all the unique numbers(once)
'''

s = set()
n = int(input("Enter number : "))
s.add(n)
n = int(input("Enter number : "))
s.add(n)
n = int(input("Enter number : "))
s.add(n)
n = int(input("Enter number : "))
s.add(n)
n = int(input("Enter number : "))
s.add(n)
n = int(input("Enter number : "))
s.add(n)
n = int(input("Enter number : "))
s.add(n)
n = int(input("Enter number : "))
s.add(n)
print(s)'''

# Question2 . what will be the lenght of the following set

s = set()
s.add(20)
s.add(20.0)
s.add('20') #it checks only value if both are seame, it doesn't see datatype
print(s)
print(len(s))

