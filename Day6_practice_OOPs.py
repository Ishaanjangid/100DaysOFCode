
class Vehicle:
    color = "White"
    def __init__(self,max_speed,mileage,name):
        
        self.max_speed = max_speed
        self.mileage = mileage
        self.name = name

    def seating_capacity(self,capacity):
        print(f"Vehicle: {self.name}, Capacity: {capacity}")

class Bus(Vehicle):
    def __init__(self,max_speed,mileage,name):
        super().__init__(max_speed,mileage,name)

    def info(self):
        print(f"Vehicle Name: {self.name} Speed: {self.max_speed} Mileage: {self.mileage}")

    def seating_capacity(self, capacity = 60):
        return super().seating_capacity(capacity)

class Car(Vehicle):
    pass

bus = Bus(100,10,"Volvo")
car = Car(241,432,"423")
car.color