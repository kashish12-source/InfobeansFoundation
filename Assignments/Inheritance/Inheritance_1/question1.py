# 1. Animal Sound System

# Create parent class Animal and child classes:

# Dog
# Cat
# Cow

# Override sound() method.

from abc import ABC ,abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass 

class Dog(Animal):
    def sound(self):
        print("Bhow Bhow")
    
class Cat(Animal):
    def sound(self):
        print("meow meow")
    
class Cow(Animal):
    def sound(self):
        print("owwwwww owwww")

d1 = Dog()
c1 = Cat()
c2 = Cow()
d1.sound()
c1.sound()
c2.sound()
