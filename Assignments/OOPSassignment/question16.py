# # 16. Write a Java program to create a class called "Shape" with abstract methods for calculating area and perimeter, and subclasses for "Rectangle", "Circle", and "Triangle".

from abc import ABC, abstractmethod
import math

# Parent class
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


# Child class 1
class Rectangle(Shape):

    def __init__(self, length, breadth):
        self.__length = length
        self.__breadth = breadth

    def area(self):
        print("Area of rectangle:", self.__length * self.__breadth)

    def perimeter(self):
        print("Perimeter of rectangle:", 2 * (self.__length + self.__breadth))


# Child class 2
class Circle(Shape):

    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        print("Area of circle:", math.pi * self.__radius ** 2)

    def perimeter(self):
        print("Circumference of circle:", 2 * math.pi * self.__radius)


# Child class 3
class Triangle(Shape):

    def __init__(self, side_1, side_2, side_3):
        self.__side_1 = side_1
        self.__side_2 = side_2
        self.__side_3 = side_3

    def area(self):
        # Heron's formula
        s = (self.__side_1 + self.__side_2 + self.__side_3) / 2

        result = math.sqrt(
            s * (s - self.__side_1) *
            (s - self.__side_2) *
            (s - self.__side_3)
        )

        print("Area of triangle:", result)

    def perimeter(self):
        print("Perimeter of triangle:",
              self.__side_1 + self.__side_2 + self.__side_3)


# Creating objects
r = Rectangle(10, 5)
c = Circle(7)
t = Triangle(3, 4, 5)

r.area()
r.perimeter()

c.area()
c.perimeter()

t.area()
t.perimeter()
