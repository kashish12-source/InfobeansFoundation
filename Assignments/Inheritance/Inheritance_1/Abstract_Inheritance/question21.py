
# Shape area calculator
# abstract class shape
# derived class = circle, rectangel,triangel 

from abc import ABC , abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass 

class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius
    
    def area(self):
        print(f"Area of circle is : {3.14*self.__radius**2}")
    
    def get_radius(self):
        return self.__radius

class Rectangle(Shape):
    def __init__(self, length , breadth):
        self.__length = length
        self.__breadth = breadth
    
    def area(self):
        print(f"Area of rectangle is : {self.__length*self.__breadth}")
    
    def get_length(self):
        return self.__length
    
    def get_breadth(self):
        return self.__breadth
    
class Triangle(Shape):
    def __init__(self, side_1,side_2,side_3):
        self.__side_1=side_1
        self.__side_2 = side_2
        self.__side_3 =side_3
    
    def area(self):
        print(f"Area of the triangle is : {self.__side_1 * self.__side_2 * self.__side_3}")
    
    def get_side_1(self):
        return self.__side_1

    def get_side_2(self):
        return self.__side_2

    def get_side_3(self):
        return self.__side_3

c = Circle(45)
r = Rectangle(20,30)
t = Triangle(1,2,3)
c.area()
r.area()
t.area()


