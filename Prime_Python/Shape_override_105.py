class Shape:
    def area(self):
        print("Area not defined")

class Circle(Shape):
    def __init__(self, r):
        self.r = r
        
    def area(self):
        return 3.14 * self.r * self.r

class Rectangle(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b
        
    def area(self):
        return self.l * self.b

class Triangle(Shape):
    def __init__(self, b, h):
        self.b = b
        self.h = h
        
    def area(self):
        return 0.5 * self.b * self.h

c = Circle(5)
r = Rectangle(4, 6)
t = Triangle(3, 8)

print("Circle area:", c.area())
print("Rectangle area:", r.area())
print("Triangle area:", t.area())
