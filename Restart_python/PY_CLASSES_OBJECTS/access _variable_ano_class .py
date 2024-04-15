class Vehicle:
    def __init__(self):
        self.engine='1500cc'
class Car(Vehicle):
    def __init__(self,max_speed):
        super().__init__()
        self.max_speed=max_speed
    def show(self):
        print(self.engine)
        print(self.max_speed)

c=Car(240)
c.display()
        
 
