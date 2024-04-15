class Student :
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(self.name,self.age)
s=Student("kinal",12)
print(s.name)
print(s.age)