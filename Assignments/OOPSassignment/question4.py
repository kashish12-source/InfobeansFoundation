
# 4. Write a Java program to create a class called "Circle" with a radius attribute. You can access and modify this attribute. Calculate the area and circumference of the circle.

class Circle:
    pi = 3.14
    def __init__(self, radius):
        self.__radius = radius 

    def set_radius (self,radius):
        self.__radius = radius
    
    def get_radius(self):
        return self.__radius

    def area_of_circle(self):
        
        x = self.pi
        return (x*((self.__radius)**2))

    def circumference_of_circle(self):
        x = self.pi
        return ((2*x*self.__radius))
    
radius1  = Circle(30)
print(radius1.get_radius())
radius1.set_radius(20)
print(f"area of circle is : {radius1.area_of_circle()}")
print(f"Circumference of circle is : {radius1.circumference_of_circle():.2f}")

