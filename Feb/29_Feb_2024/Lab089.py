# Hierarchical Inheritance
class Vehicle:
    def info(self):
        return "This is a vehicle"


class Car(Vehicle):
    pass

class Bicycle(Vehicle):
    pass

car= Car()
vehi=Vehicle()

print(car.info())