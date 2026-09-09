import math
class square :
    def __init__(self,side):
        self.side = side
    def area(self):
        return self.side**2

class circle:
    def __init__ (self,radius):
        self.radius = radius
    def area(self):
        return math.pi * (self.radius**2)

def show_area(shape):
    print("Area:",shape.area())

show_area(square(4))
show_area(circle(3))

