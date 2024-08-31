'''
Topic : Tuples

Tuples - Tuples can be created with open parenthesis()
         Tuples are immutable sequence of Data(Doen't change)
         Tuple are collecction of Different Datatypes
         once created we can change the values
         Tuples Can be done Indexing and slicing
'''
# Creating Tuple
t = ()
print(type(t))

# Indexing
t1 = (1, 2, 3, 3, 4, 5, "Hero", True, 5+4j)
print(t1)
# print(t1[[0]] = "Raj") #shows error we canot do in tuple
print(t1[5])
print(t1[6])
# Slicing
print(t1[0:6])
print(t1[3:6])
print(t1[-3:-1])


# Converting tuple into ist
print(list(t1))

# Converting list into tuple
l = [1,2,3,4,5,6]
print(tuple(l))

# Count()
print(t1.count(3))

# Index()
print(t1.index("Hero"))

# Max() and Min()
t2 = (1, 3, 5, 6, 8, 10)
print(max(t2))
print(min(t2))

# sum() - Findin sum of the elements present in the tuple
print(sum(t2))

# Ques.Check how many occurence of 0 is present in tuple
a= (2,2,2,42, 234, "Harry")
print(a.count(2))
# print(a)
