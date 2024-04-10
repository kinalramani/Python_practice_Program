class person:
    def __init__(self,fname='kinal',lname='ramani',age=21,city='surat'):
        self.fname=fname
        self.lname=lname
        self.age=age
        self.city=city
    def info_person(self):
        return f'my name is {self.fname}{self.lname} i am {self.age} old and i lives in {self.city} .'
p=person()
print(p.info_person())
p1=person("juijd","usgh",54,"vadodara")
print(p1.info_person())