class Student:
    def __init__(self,name,roll_no,age):
        self.name=name
        self.roll_no=roll_no
        self.age=age
    def show(self):
        print("name:",self.name,"roll_no:",self.roll_no,"age:",self.age)
    def update(self,name,age):
        self.name=name
        self.age=age
s=Student("kinal",56,10)
s.show()
s.update("k",12)
s.show()
