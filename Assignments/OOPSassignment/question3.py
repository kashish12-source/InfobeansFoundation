# 3. Write a Java program to create a class called "Rectangle" with width and height attributes. Calculate the area and perimeter of the rectangle.

class Rectangle:
    def __init__(self , width , height):
        self.__width = width 
        self.__height = height
    
    def area_of_rectangle(self):
        return (self.__width * self.__height)
    
    def perimeter_of_rectangle (self):
        return (2*(self.__width + self.__height))

    def set_width (self, width):
        self.__width = width 

    def set_height ( self , height):
        self.__height = height
    
    def get_width (self):
        return self.__width

    def get_height(self):
        return self.__height

    
r1 = Rectangle(20,40)
area = r1.area_of_rectangle()
perimeter = r1.perimeter_of_rectangle()

print(f"Perimeter of the rectangle is : {perimeter}")
print(f"Area of the rectangle is : {area}")
