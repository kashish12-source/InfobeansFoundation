
# 31. Drawable Interface

# Interface:

# draw()

# Implement:

# Circle
# Rectangle
# Line


from abc import ABC, abstractmethod


class Drawable(ABC):

    @abstractmethod
    def draw(self):
        pass


class Circle(Drawable):

    def draw(self):
        print("Drawing a Circle")

class Rectangle(Drawable):

    def draw(self):
        print("Drawing a Rectangle")

class Line(Drawable):

    def draw(self):
        print("Drawing a Line")


c1 = Circle()
r1 = Rectangle()
l1 = Line()


c1.draw()
r1.draw()
l1.draw()
