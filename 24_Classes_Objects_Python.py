#1
class MyClass:
    x = 5

#2
p1 = MyClass()
print(p1.x)

#3
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)
print(vars(p1))
print(p1.name)
print(p1.age)