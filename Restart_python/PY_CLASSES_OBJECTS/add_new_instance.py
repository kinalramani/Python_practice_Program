class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
s=Student("b",7)
print(s.name)
print(s.age)

s.marks=98
print(s.name)
print(s.age)
print(s.marks)