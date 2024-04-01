class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    # def __init__(self, name, max_speed, mileage):
    #     self.name = name
    #     self.max_speed = max_speed
    #     self.mileage = mileage
    pass

b=Bus("kinal",200,8)

print(b.name)
print(b.max_speed)
print(b.mileage)

