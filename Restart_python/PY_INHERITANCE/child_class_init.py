class Student:
    def __init__(self,fname,lname,age):
        self.fname=fname
        self.lname=lname
        self.age=age
    def printname(self):
        print(self.fname,self.lname,self.age)
class Teacher(Student):
    def __init__(self,fname,lname,age):
        Student.__init__(self,fname,lname,age)
t=Teacher("kinal","ramani",12)
t.printname()