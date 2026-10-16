class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats

class Bike(Vehicle):
    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model)
        self.engine_cc = engine_cc

car = Car("Toyota", "Innova", 7)
bike = Bike("Yamaha", "R15", 155)

print("Car:", car.brand, car.model, car.seats, "seats")
print("Bike:", bike.brand, bike.model, bike.engine_cc, "cc")
