def Student_data(s_id):
    def __init__(self,s_name,s_class):
        self.s_name=s_name
        self.s_class=s_class
    def printoutput(self):
        return f"{self.s_name}{self.s_class}"
s=Student_data("ki","b")
print(s.printoutput)