class Vehicle:

    def __init__(self,color, name, max_speed, mileage):
        self.color=color
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass
b=Bus("white","bus",200,7)
c=Car("white","bus",200,7)
print("color:",b.color,",","name:",b.name,",","max_speed",b.max_speed,",","milage:",b.mileage)
print("color:",b.color,",","name:",c.name,",","max_speed",c.max_speed,",","milage:",c.mileage)
