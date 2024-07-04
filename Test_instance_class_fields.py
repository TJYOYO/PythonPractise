class Person:
    high = "180"

    def __init__(self, name, age):
        self.name = name  # instance field
        self.age = age


person1 = Person("Alice", 18)
person2 = Person("Bob", 25)

Person.high = "200"
print(f"Person.high = {Person.high}")  # Class fields, if change it , all instances will be changed.

print(f"person1.name = {person1.name}")
print(f"person1.high = {person1.high}")

print(f"person2.age = {person2.age}")
print(f"person2.high = {person2.high}")
