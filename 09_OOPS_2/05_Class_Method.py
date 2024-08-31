"""
Class Method :- A class method is bound to the class & receives the class as an Impicit first Arguements

Note :-
"""
# Method 1 :- Person.name
# class Person:
#     name = "Tony"

#     def Change_name(self, name):
#         Person.name = name

# p = Person()
# p.Change_name("Stark")
# print(p.name)
# print(Person.name)

# Method 2 - Self.__class__.name = "Rahul"
class Person:
    name = "Tony"

    def Change_name(self, name):
       self.__class__.name = "Rahul"

p = Person()
p.Change_name("Stark")
print(p.name)
print(Person.name)
