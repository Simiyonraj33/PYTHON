class Shape:
    def area(self):
        return "No dimensions provided"
    
    def display(self):
        print(self.__class__.__name__, "Area:", self.area())

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    def area(self):
        return self.length * self.breadth

class Cuboid(Shape):
    def __init__(self, length, breadth, height):
        self.length = length
        self.breadth = breadth
        self.height = height
    
    def area(self):
        return 2 * (self.length * self.breadth + self.breadth * self.height + self.height * self.length)

class Triangle(Shape): 
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self): 
        return 0.5 * self.base * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

shapes = [Rectangle(5, 10), Cuboid(5, 10, 15), Triangle(5, 10), Circle(5), Shape()]
for s in shapes:
    s.display()
