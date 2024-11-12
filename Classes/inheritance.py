class Vehicle:
    def vehicle_method(self):
        print(f"This is a parent vehicle class method")


any_vehicle = Vehicle()
any_vehicle.vehicle_method()

class Car(Vehicle): # Car class inherits Vehicle class
    def car_method(self):
        print(f"this is a child car class method")


a_car = Car()
a_car.car_method() # a_car can access its own methods
a_car.vehicle_method() # a_car can also access its parent class, class Vehicle's, methods

class Bicycle(Vehicle): # a class can have multiple children
    def cycle_method():
        print(f"This is a child cycle method")


my_bike = Bicycle()
my_bike.cycle_method()
my_bike.vehicle_method()

cla