# 2. Vehicle System

# Create parent class Vehicle.

# Child classes:

# Car
# Bike
# Bus

# Add methods:

# start()
# stop()

from abc import ABC,abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass 

    @abstractmethod
    def stop(self):
        pass 

    
class Car(Vehicle):

    def __init__(self):
        print("Press 1 to start the car\nPress 2 to stop the car")

        self.__choice = int(input("Enter your choice here: "))

        if self.__choice == 1:
            self.start()

        elif self.__choice == 2:
            self.stop()

        else:
            print("\nPlease enter a valid choice")

    def start(self):
        print("\nYour car has been started")

    def stop(self):
        print("\nYour car has been stopped")




class Bike(Vehicle):
    def __init__(self):
        print("\nPress 1 to start the car\nPress 2 to stop the car")

        self.__choice = int(input("Enter your choice here: "))
        if self.__choice == 1:
            self.start()
        elif self.__choice == 2:
            self.stop()
        else:
            print("\nYour choice is invalid ")


    def start(self):

        print("\nYour Bus has been started ")
    
    def stop(self):
        print("\nYour Bus has been stoped ")
    

class Bus(Vehicle):
    
    def __init__(self):
        print("\nPress 1 to start the Bus \nPress 2 to stop the Bus")
        self.__choice = int(input("Enter you choice here : "))

        if self.__choice  == 1 :
            self.start()
        elif self.__choice == 2:
            self.stop()
        else :
            print("\nYour choice is invalid ")

    
    def start(self):
        print("\nYour Bus has been started ")
    
    def stop(self):
        print("\nYour Bus has been stoped ")



c = Car()
b1 = Bike()
b2 = Bus()
