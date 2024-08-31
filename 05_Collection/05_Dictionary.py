"""
Topic :- Dictionary

Dictionary - Dictionary stores Data in key value pair
             it is unordered
             it is mutable and do not have duplicate value
             it is indexed - we can access through key
             cannot contain duplicate dictionary
"""

# Creating null or empty dict
d = {}
print(type(d))

info = {
    # "key" : Value - pairs
    "key" : "vaue",
    "name " : "skillls",
    "learning" : "coding"
}
print(info)

# using Diff Datatypes in Dictionary
info1 = {
    "name " : "skillls",
    "age" : 23,
    "learning" : "coding",
    "is_male" : True,
    "percentage" : 99.9
}
print(info1)

# Using list and Tuple in Dictionary
list = {
    "name " : "skillls",
    "age" : 23,
    "subject" : ["Python", "Java","C"  , "Css"],
    "tuple" : ("Dictionary", "Sets"),
    "learning" : "coding",
    "is_male" : True,
    "percentage" : 99.9
}
print(list)

# Giving Key as integer number and Value as String
d1 = {
    12 :"Integer",
    12.5 :"float",
}
print(d1)
# We can use tuple only as key bcoz tuple is immutable
# We can not create duplliacte key as same key

dict = {
    "name " : "skillls",
    "age" : 23,
    "learning" : "coding",
    "is_male" : True,
    "percentage" : 99.9
}
print(dict)

# Aceesing key as indexing
print(dict["name "])
print(dict["age"])

# Assigning - updating value
dict["name "] ="Chandria" #overwrite
print(dict)
# Adding key value pairs
dict["name1"] ="Dhanush"
print(dict)

# Creating empty dictionary and adding key value pair
null_dict={}
null_dict["name"] = "Dhanush"
null_dict["Profession"] = "Coder"
null_dict["Salary"] = "100000"
print(null_dict)

# Nested Dictionary
stu = {
    "name" : "Rahul Kumar",
    "Subject" : {
        "phy" : 23,
        "chem" : 23,
        "python" : 100,
    }
}
print(stu)
# Acessing key in nested Dictionary
print(stu["Subject"])
print(stu["Subject"]["python"])

''' Dictionary Methods   '''
# Keys() - return all keys
print(stu.keys())

# values() - return all values
print(stu.values())

# Update() - inserts thee speccified itemss on the dictionaary

print(stu.update({"Key": "value"}))



# items() -it returns all key value pairs in tuples
print(stu.items())

# get() - returns the key according to value
print(stu.get("name2"))