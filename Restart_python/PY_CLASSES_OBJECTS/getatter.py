class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print("name:",self.name,"age:",4)
s=Student("bhumi",75)
print(getattr(s,"name"))
print(s.age)