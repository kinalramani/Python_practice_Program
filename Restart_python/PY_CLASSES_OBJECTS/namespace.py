class Student:
    def __init__(self,s_id,s_name,s_class):
        self.s_id=s_id
        self.s_name=s_name
        self.s_class=s_class
s=Student(4,"ki","c")
print(s.__dict__)