class Vehicle:
    def __init__(self, speed, mileage):
        self.speed = speed
        self.mileage = mileage 

    def get_info(self):
        return self.speed, self.mileage
    
class Car(Vehicle):
    def __init__(self, speed, mileage, fuel):
        super().__init__(speed, mileage)
        self.fuel = fuel

    def get_info(self):
        return self.speed, self.mileage, self.fuel
    
class Bike(Vehicle):
    def __init__(self, speed, mileage, type):
        super().__init__(speed, mileage)
        self.type = type

    def get_info(self):
        return self.speed, self.mileage, self.type

vehicle1 = Vehicle(420, "mp/h")
car1 = Car(350, "km/h", 2.2)
bike = Bike(20, "km/p", "sport")

print(vehicle1.get_info())
print(car1.get_info())
print(bike.get_info())