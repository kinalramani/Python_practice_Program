class Student:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def show(self):
        print("fname:",self.fname,"lname:",self.lname)
s=Student("k",9)
s.show()