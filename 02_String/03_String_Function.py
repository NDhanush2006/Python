"""
Topic - String Methods (or) Function
String Methods :-python provides a set of built in methodsthat we can use to after and modify the strings
"""

# Strings are immutable
a = "Harry"
print(len(a))

# upper() - The upperr() mathod converts a string to uppercase
a = "Dhanush"
print(a.upper())

# lower() - The upperr() mathod converts a string to lowercase
a = "DHANUSH"
print(a.lower())

# strip() -The strip method removes any while spaces before and after the String and prints the trailing characters like-(!)
a = "!*Harry!!!!!!!!!!!!!!"
print(a.strip())

# rstrip() -The strip method removews any trailing characters exept in staring 
a = "!Harry!!!!!!!!!!!!!!"
print(a.rstrip("!!"))

# replace()- The replace() method replaces all occurences of a string with another string with all occurences or names.
b = "John"
print(b.replace("John","Ram"))

# split()- the split() method splits the given string at the specified instance and returns seperated strings as list items.
b = "John Fernadus"
print(b.split(" ")) 

# capitalize() - The capitalize () method turns only the first character or letter of the string to uppercase and the rest of the character s are turnedd to lowercase.the string has no effect if the first character is already uppercase.
capital = "intro to Web Development"
print(capital.capitalize())

# center() - The center method aligns the string to the center as per the parameters given by the user.
center = "intro to Web Development"
print(center.center(100))
# it also provide padding character .it will fill the rest of the fill characters provided by the user eg:-
print(center.center(50, "*"))

# count() -The count() method return the numbeer of items the given value occured within the given string
coun ="I am Dhanush, the boy name is Dhanush"
print(coun.count("Dhanush"))

# Endswith()- the endwith() method checks if the string ends with a given value. if yes than return (True), else returns (False)


end = "Welcome to the console!!!"
print(end.endswith("!"))
# we can even check for a value in between the string by providing startvand end with the Index.eg:-
end = "Welcome to the console!!!"
print(end.endswith("to", 4, 10))

# find() - The find() method searchesfor the first occurences of the given value and returns the index where it is present, if the given value is absent from the string then written -1
fin = "He is very good boy and his cute name is Abi"
print(fin.find("is"))

#index() - The index() method searches for the first occurences of the given value and returns the index where it is present. If given value  is absent from the string then raise then raise an exception and print(ValueError: substring not found).
'''fin = "He is very good boy and his cute name is Abi"
print(fin.index("ok"))'''

# isalnum() - The isalnum() method reeturns true only if the entire string only consists of A-Z, a-z, 0-9.If any other characters or punctuations are present, then it returns False.
str1 = "WelcomeToconsole"
print(str1.isalnum())

# isalpha() -The isalpha() method returns true only if the entire string only consists of A-Z, a-z .If any other characters or punctuations are numbers( 0-9)present, then it returns False.
str1 = "WelcomeToconsole"
print(str1.isalpha())

# islower() -The islower() method returns True if all the charaacters in the string are lower case, else it returns False.
str2 = "hello world"
print(str2.islower())

# isprintable() - The isprintable() method returns True if all the value within the given string is printabble, if not it return False 
str2 = "hello world\n"
print(str2.isprintable())

# isspace() - The isspace() method returns True only and only if the string contains white spaces, else returns false
t = " " #using spacebar
print(t.isspace())

# istitle() -The istitle() method returns True only if the first letter of eacch word of the string is capitalize, else it returns False
t = "Helloo World Is "
print(t.istitle())

#  isupper() -The isupperr() method returns True if all the charaacters in the string are uppercase, else it returns False.
a = "DHANUSH"
print(a.isupper())

# Startswith()-t he startswith() method checks if the string starts with a given value. if yes than return (True), else returns (False)

c = "Python is best"
print(c.startswith("Python"))

# Swapcase() - It converts Lowercase to uppercase and uppercase to lowercase
a = "DHANUSH"
print(a.swapcase())

# title() - it capitalizes each letter of the word within the string
d = " He's Don King and he is cricketer"
print(d.title())

