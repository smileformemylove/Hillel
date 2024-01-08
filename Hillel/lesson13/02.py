import math

from task01 import Point

class Circle(Point):

    def __init__(self, radius, x = 0, y = 0):
        super().__init__(x, y)
        self.radius = radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __str__(self):
        return f'Circle({self.x}, {self.y}), radius = {self.radius}'

    def __add__(self, other):
        new_obj =  super().__add__(other)
        radius = self.radius + other.radius
        return Circle(radius, new_obj.x , new_obj.y)

    def __sub__(self, other):
        if self.radius == other.radius:
            return Point(self.x - other.x, self.y - other.y)
        else:
            new_radius = abs(self.radius - other.radius)
            new_x = self.x - other.x
            new_y = self.y - other.y
            return Circle(new_x, new_y, new_radius)

    def area(self):
        return round(math.pi * (self.radius ** 2), 3)


circle_1 = Circle(5, 1)

print(circle_1.radius)
print(circle_1.x)
print(circle_1.y)
print(circle_1)
print(circle_1.area())

circle_2 = Circle(2, 4, 8)
print(circle_2)
print(circle_1 == circle_2)
print(circle_1 + circle_2)
print(circle_1 - circle_2)