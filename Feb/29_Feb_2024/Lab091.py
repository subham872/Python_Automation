# polymorphism
# poly means -Many
# Morphism means form


class Shape:
    def area(self):
        print("Area of shape")


class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

shape1=Rectangle(4,5)
print(shape1.area())

shape2=Circle(10)
print(shape2.area())