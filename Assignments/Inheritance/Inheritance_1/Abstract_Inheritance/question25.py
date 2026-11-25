
# 25. Ride Booking App

# Abstract:

# Ride

# Derived:

# BikeRide
# CabRide
# AutoRide

# Calculate fare.

from abc import ABC ,abstractmethod

class Ride (ABC):

    @abstractmethod
    def display_rent(self):
        pass 

    @abstractmethod
    def calculate_fare(self):
        pass 

    @abstractmethod
    def validate_id(self):
        pass 


collection = []
def add_vehicle(obj):
    collection.append(obj)

class RegisterVehicle:
    def __init__(self, name ,model,id,price):
        self.__name = name 
        self.__model = model 
        self.__price = price 
        self.__id  =id 
        


    def get_price(self):
        return self.__price 

    def get_name (self):
        return self.__model

    def get_id(self):
        return self.__id

class BikeRide(Ride):
    def __init__(self, id):
        self.__id = id 
        self.__validate_id = False
        self.__obj_id = None
        self.__price = None
    
    
    def validate_id(self):
        for obj in collection:
            if obj.get_id() == self.__id:

                self.__validate_id = True
                self.__obj_id = obj
                print("Vehicle validated")
                return True
        print("Vehicle is not validated")
        return False


    def display_rent(self):
        
        if self.__validate_id:
            obj = self.__obj_id
            print(f"The price of the ride is :{obj.get_price()} per km")

            self.__price = obj.get_price()


    def calculate_fare(self):
        dis = int(input("Enter the distance here : "))

        if self.__validate_id:
            print(f"Total fair is : {self.__price *dis}")



class AutoRide(Ride):
    def __init__(self, id):
        self.__id = id 
        self.__validate_id = False
        self.__obj_id = None
        self.__price = None
    
    
    def validate_id(self):
        for obj in collection:
            if obj.get_id() == self.__id:

                self.__validate_id = True
                self.__obj_id = obj
                print("Vehicle validated")
                return True
        print("Vehicle is not validated")
        return False


    def display_rent(self):
        
        if self.__validate_id:
            obj = self.__obj_id
            print(f"The price of the ride is :{obj.get_price()} per km")

            self.__price = obj.get_price()


    def calculate_fare(self):
        dis = int(input("Enter the distance here : "))

        if self.__validate_id:
            print(f"Total fair is : {self.__price *dis}")



class CarRide(Ride):
    def __init__(self, id):
        self.__id = id 
        self.__validate_id = False
        self.__obj_id = None
        self.__price = None
    
    
    def validate_id(self):
        for obj in collection:
            if obj.get_id() == self.__id:

                self.__validate_id = True
                self.__obj_id = obj
                print("Vehicle validated")
                return True
        print("Vehicle is not validated")
        return False


    def display_rent(self):
        
        if self.__validate_id:
            obj = self.__obj_id
            print(f"The price of the ride is :{obj.get_price()} per km")

            self.__price = obj.get_price()


    def calculate_fare(self):
        dis = int(input("Enter the distance here : "))

        if self.__validate_id:
            print(f"Total fair is : {self.__price *dis}")



# Registering vehicles

v1 = RegisterVehicle("Kashish", "Honda Shine", 101, 10)
v2 = RegisterVehicle("Koshiki", "Maruti Swift", 102, 15)
v3 = RegisterVehicle("Rahul", "Auto Rickshaw", 103, 12)

add_vehicle(v1)
add_vehicle(v2)
add_vehicle(v3)


# Creating BikeRide object

b = BikeRide(101)

print("\n----- BIKE RIDE -----")
b.validate_id()
b.display_rent()
b.calculate_fare()


# Creating AutoRide object

a = AutoRide(103)

print("\n----- AUTO RIDE -----")
a.validate_id()
a.display_rent()
a.calculate_fare()


# Creating CarRide object

c = CarRide(102)

print("\n----- CAB RIDE -----")
c.validate_id()
c.display_rent()
c.calculate_fare()
