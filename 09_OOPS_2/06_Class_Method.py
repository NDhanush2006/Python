class Person:
    name = "Tony"

    @classmethod
    def Change_name(cls, name):
        cls.name =name
        

p = Person()
p.Change_name("Stark")
print(p.name)
print(Person.name)