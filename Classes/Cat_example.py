class Cat:
    def __init__(self, name, age, breed): # a function you need if your class is a blueprint for an object
        self.name = name
        self.age = age
        self.breed = breed

    def meow(self):
        print(f"{self.name} says meow")

    def get_info(self):
        print(f"{self.name} is {self.age} years old {self.breed} cat")

    def birthday(self):
        self.age += 1
    
    def eats_tea(self, food_item):
        print(f"{self.name} is eating {food_item}")

mork = Cat(name='Mork', age=2, breed='tuxedo') # this is an object, i.e., an instance of the cat class
mork.meow()

