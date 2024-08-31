'''
Topic : - ForLoop with else
'''

# ForLoop with else
# We use For loop with else if the for loop is exhausted , the else will print to know the For loop is executed fully
l = [ 2, 3, 4, 5, 6, 7, 8]
for i in l:
    print(i)
else:
    print("These will be Executed once For Loop Exhausted")

# Forloop else with loop
l = [ 2, 3, 4, 5, 6, 7, 8]
for i in l:
    if i == 5:
        print(i)
        break
else:
    print("These will be Executed once For Loop Exhausted")


# Printing sum of all elements present in the list using For Loop
l = [ 2, 3, 4, 5, 6, 7, 8]
b = 0
for i in l:
    b = b + i 
print(b)

# For a given list l2 with Diff datatypes, print a seperate list of each type of data
l2 = [ 2, 3, 4, 323,"Roshan", "Harry", "Ben", True, False]
l_int = []
l_str = []
l_bool = []
for i in l2:
    if type(i) == int:
        l_int.append(i)
    elif type(i) == str:
        l_str.append(i)
    elif type(i) == bool:
        l_bool.append(i)
print(l_bool)    
print(l_int)
print(l_str)

# Printing Dictionary - it only print keys , not value
l3 ={"name":"Dhanush", "age": 18, "Profession": "Coder, Programmer", "Salary": 200000}
# for i in l3:
#     # print(i)

# printing key value pair at same time -use Dictionary method and see in forloop(keys(), Value,)
for i in l3.items():
    print(i)

