#Thomas Cubstead
#OOP Review Project
#Shapes_Hierarchy
#9/21/25
#This program demonstrates the use of OOP concepts to calculate the area of different shapes

import math
from abc import ABC, abstractmethod

#abstract base class used as the foundation for all other classes
class BasicShape(ABC):
    def __init__(self, name="shape"):
        self.area = 0.0
        self.name = name

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, value):
        self._area = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        
    @abstractmethod
    def calc_area(self):
        pass

#circle class inherits from basic shape 
class Circle(BasicShape):
    def __init__(self, x, y, r, n="circle"):
        super().__init__(n)
        self._x_center = x
        self._y_center = y
        self._radius = r
        self.calc_area()

    def calc_area(self):
        self.area = math.pi * (self._radius ** 2)
    
    @property
    def y_center(self):
        return self._y_center

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value
        self.calc_area()

#rectangle class inherits from basic shape nonequilateral sides
class Rectangle(BasicShape):
    def __init__(self, l, w, n="Rectangle"):
        super().__init__(n)
        self._length = l
        self._width = w
        self.calc_area()

    def calc_area(self):
        self.area = self._length * self._width

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        self._length = value
        self.calc_area()

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value
        self.calc_area()


#square class inherits from rectangle with equallateral sides
class Square(Rectangle):
    def __init__(self, s, n="square"):
        self._side = s
        super().__init__(s, s, n)
        self.name = n

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        self._side = value
        self.length = value
        self.width = value
        self.calc_area()

if __name__ == "__main__":
    print("--- Polymorphism Check ---")

    shapes = [
        Circle(0, 0, 4, "circle_1"),
        Circle(1, 1, 9, "Circle_2"),
        Rectangle(10, 20, "Rectangle_1"),
        Rectangle(30, 20, "Rectangle_2"),
        Square(10)
    ]

    #test cases
    for shape in shapes:
        print(f"{shape.name} Area: {shape.area:.5f}")

    print("\n--- Getter/Setter check ---")

    c1 = shapes[0]
    print(f"{c1.name} Current: {c1.radius} {c1.area:.5f}")
    c1.radius *= 2
    print(f"{c1.name} Doubled: {c1.radius} {c1.area:.5f}")

    r1 = shapes[2]
    print(f"{r1.name} Current: {r1.length} {r1.width} {r1.area:.5f}")
    r1.length *= 2
    r1.width *= 2
    print(f"{r1.name} Doubled: {r1.length} {r1.width} {r1.area:.5f}")

    s1 = shapes[4]
    print(f"{s1.name} Current: {s1.side} {s1.area:.5f}")
    s1.side *= 2
    print(f"{s1.name} Doubled: {s1.side} {s1.area:.5f}")
