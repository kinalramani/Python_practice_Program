class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def Info_person(self):
        return f'my name is {self.name} and i am {self.age} year old'
p=Person("kinal",21)
print(p.Info_person())