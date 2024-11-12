class Shape(object): # how to make an abstract class
    def calc_perimeter(self):
        raise NotImplementedError("Please Implement this method")
    

class Triange(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def calc_perimeter(self):
        perimeter