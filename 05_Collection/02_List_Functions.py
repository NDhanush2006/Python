'''
Topic : List Function and Methods
'''

l = [ 1, 2, 3, 3.56, "Apple", True]
print(l)

# Repeating list number of times
print(l * 2)
# Repeating string number of times
s = "Harry"
print(s * 2)

# Concatenating(Adding) Two list or Append list
l1=[1,2,3,4]
print( l + l1)

# Finding numbeer of elements in the list
print(len(l))

# Membership operator in list
print("Apple" in l) #True

# Finding Maximum or biggest number in the list
print(max(l1))

#Finding Minimum or smallest number in the list 
print(min(l1))

#Finding Maximum or biggest Alphabt in the string of in the list 
l2 = ["abc", "def", "ghi", "jkl"]
print(max(l2))

#Finding Minimum or smallest Alphabt in the string of in the list 
print(min(l2))

#       1       0
l3 = [True , False]
print(max(l3))
print(min(l3)) 


# inserting (or) Append element or number in the ist
# Append() - it adds String or number at the end of the list (or) Append object to the end of the list.
l4 = [1, 2, 3, 4, 5, 6]
l4.append(7)
l4.append("Hero")
print(l4)

# Insert() - Insert object before index. adding element or string middle or between the list
l4.insert(1,"First")
print(l4)

# pop() -it removes the last element available int the list
l4.pop() 
print(l4)

# pop(Index) -
l4.pop(3)
print(l4)

# reverse() - to reverse the given list
l4.reverse()
print(l4)

# sort() - To arrange the list in Ascending order
l1.sort()
print(l1)

# Reverse=True - if it is ascending order it reverse to descending oreder , else if it is descending orederr it reverse to ascending oreder
l5 = ["College", "School", "Job"]
l5.sort(reverse=True)
print(l5)

# To Putting all list in one list to join Together
# print([l,l1,l2,l3,l4,l5])

# list in list
l5 = [ l , l1, l4]
print(l5)
print(len(l5))
# indexing list in list
# l5[1][2]

print(l5)

# Count()-Returns the number of times the specified item appears on the list
fruits = [ 1,2,2, "Banana", "cherry"," grapes"]
count = fruits.count(2)
print(count)

# Extend() -Extends the lists by appending all the items from iterables
fruits.extend(["orange","Red"])
print(fruits)

# copy() - Returns the shallow copy of the list
copy_first= fruits.copy()
print(copy_first)