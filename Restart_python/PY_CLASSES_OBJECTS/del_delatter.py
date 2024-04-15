class Student:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
s=Student("udhjc","dbdc")
print(s.fname,s.lname)


del s.fname
print(s.fname)
# print(delattr(s,"fname"))