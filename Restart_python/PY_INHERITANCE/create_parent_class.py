class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def printname(self):
        return f"{self.fname} {self.lname}"
p=Person("kinal","ramani")
print(p.printname())