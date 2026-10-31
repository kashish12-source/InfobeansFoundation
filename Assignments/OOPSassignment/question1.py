# 1. Write a Java program to create a class called "Person" with a name and age attribute. Create two instances of the "Person" class, set their attributes using the constructor, and print their name and age.

class Person:
    def __init__(self, name , age):
        self.__name = name 
        self.__age = age 

    def set_name (self,name):
        self.__name = name

    def set_age(self,age):
        self.__age = age

    def get_name (self):
        print(self.__name)
    
    def get_age(self):
        print(self.__age)

    def display(self):
        print(f"Name = {self.__name}")
        print(f"Age = {self.__age}")

p1 = Person("Kashish",20)
p2 = Person("Koshiski", 20)
p1.display()
p2.display()

p2.set_name("keshav")
p2.get_name()

p2.display()
