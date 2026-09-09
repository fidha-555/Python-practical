class Shape:
    def draw(self):
        return"Drawing Shape.."
class triangle(Shape):
    def draw(self):
        return"Drawing Triangle.."
class circle(Shape):
    def draw(self):
        return"drawing circle"
shapes = [triangle(),circle()]
for s in shapes:
    print(s.draw())