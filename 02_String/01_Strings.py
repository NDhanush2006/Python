# string -In python, anything that you enclose between single or double quote marks is coonsidered as string. A string is essentially a sequence or array of textual data 

name = "Harry"
friend = "Rohan"
anotherfriend = 'krish'

print("Hello ," + name)


# Singleline string.
fruit ="He said, \"I wants to eat an apple"
fruit ='He said, \'I wants to eat an apple'

print(fruit)

# (or)
fruit ='He said, "I wants to eat an apple'
fruit ="He said, 'I wants to eat an apple"
print(fruit)

# Multiline string
lol ="""A Variable 
is a name given to a memory location in program.,
(or) variable is like a container which used to store data. 
data ."""

ok ='''A Variable 
is a name given to a memory location in program.,
(or) variable is like a container which used to store data. 
data .'''

print(lol)
print(ok)

# indexing
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
#print(name[5]) #throws an error

# For loop (just practice)
for character in name:
    print(character)