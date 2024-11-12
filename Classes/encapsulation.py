# Bad example, doesn't adhere to encapsulation
class Car:
    def __init__(self, model):
        self.model = model


# my_car = Car('Vauxhall')
# print(my_car.model)


# Good practice
class GoodCar:
    def __init__(self, model):
        self.set_model(model)
    def set_model(self, model):
        self._model = model
    def get_model(self):
        return self._model

my_car_new = GoodCar('Astra')
my_car_new.set_model("Commander")
print(my_car_new.get_model())