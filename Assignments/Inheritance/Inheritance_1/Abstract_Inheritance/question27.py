# 27. Transport Fare System

# Abstract:

# Transport

# Derived:

# Train
# Flight
# Bus

# Implement ticket pricing.

from abc import ABC ,abstractmethod

class Transport(ABC):

    @abstractmethod
    def calculate_fare(self):
        pass 

    @abstractmethod
    def validate_id(self):
        pass 

    @abstractmethod
    def display_details(self):
        pass 

collection = []
def add_to_collection (obj):
    collection.append(obj)
    print("Object is added successfully.....")


class RegisterTransport:
    
    def __init__(self,name ,id,category,time,price):
        self.__name = name 
        self.__id = id 
        self.__category = category
        self.__time = time 
        self.__price = price 

    def get_name (self):
        return self.__name 

    def get_id (self):
        return self.__id

    def get_category(self):
        return self.__category
    
    def get_time (self):
        return self.__time 

    def get_price (self):
        return self.__price 

class Train(Transport):
    def __init__(self,id):
        self.__id = id 
        self.__validate_id = False
        self.__obj = None 

    def validate_id(self):
        for obj in collection:
            if obj.get_id() == self.__id:
                print("The transport is validated successfully")
                self.__obj = obj 
                self.__validate_id = True
                return True
        print("Validation fail ")
        return False
    
    def display_details(self):
        if self.__validate_id:
            print(f"Name : {self.__obj.get_name()}")
            print(f"Category : {self.__obj.get_category()}")
            print(f"Time : {self.__obj.get_time()}")
            print(f"Price/km : {self.__obj.get_price()}")
        else:
            print("Details can't be shown ")
    
    def calculate_fare(self):
        distance = int(input("Enter the distance : "))

        if self.__validate_id:
            print(f"The total fare for your journey { self.__obj.get_price() *distance} rupees per km")
    
class Flight(Transport):
    def __init__(self,id):
        self.__id = id 
        self.__validate_id = False
        self.__obj = None 

    def validate_id(self):
        for obj in collection:
            if obj.get_id() == self.__id:
                print("The transport is validated successfully")
                self.__obj = obj 
                self.__validate_id = True
                return True
        print("Validation fail ")
        return False
    
    def display_details(self):
        if self.__validate_id:
            print(f"Name : {self.__obj.get_name()}")
            print(f"Category : {self.__obj.get_category()}")
            print(f"Time : {self.__obj.get_time()}")
            print(f"Price/km : {self.__obj.get_price()}")
        else:
            print("Details can't be shown ")
    
    def calculate_fare(self):
        distance = int(input("Enter the distance : "))

        if self.__validate_id:
            print(f"The total fare for your journey { self.__obj.get_price() *distance} rupees per km")
    
class Bus(Transport):
    def __init__(self,id):
        self.__id = id 
        self.__validate_id = False
        self.__obj = None 

    def validate_id(self):
        for obj in collection:
            if obj.get_id() == self.__id:
                print("The transport is validated successfully")
                self.__obj = obj 
                self.__validate_id = True
                return True
        print("Validation fail ")
        return False
    
    def display_details(self):
        if self.__validate_id:
            print(f"Name : {self.__obj.get_name()}")
            print(f"Category : {self.__obj.get_category()}")
            print(f"Time : {self.__obj.get_time()}")
            print(f"Price/km : {self.__obj.get_price()}")
        else:
            print("Details can't be shown ")
    
    def calculate_fare(self):
        distance = int(input("Enter the distance : "))

        if self.__validate_id:
            print(f"The total fare for your journey { self.__obj.get_price() *distance} rupees per km")
    
t1 = RegisterTransport("Rajdhani Express", 101, "AC", "10:30 AM", 5)
t2 = RegisterTransport("Shatabdi Express", 102, "Executive", "02:00 PM", 8)
t3 = RegisterTransport("Vande Bharat", 103, "AC Chair Car", "06:00 PM", 10)

f1 =  RegisterTransport("Air India",1001,"Busines","01:39 AM", 1829)
f2 =  RegisterTransport("International",1002,"Local","09:39 PM", 429)
f3 = RegisterTransport("Indigo",1003,"Economy","10:39 AM", 829)

b1 =  RegisterTransport("Hans Travels",201,"AC","10:39 AM", 829)
b2 =  RegisterTransport("Samay shatabdi",202,"Non -AC","10:39 AM", 829)
b3 =  RegisterTransport("ashoka",203,"AC","10:39 AM", 829)


add_to_collection(t1)
add_to_collection(t2)
add_to_collection(t3)

add_to_collection(f1)
add_to_collection(f2)
add_to_collection(f3)

add_to_collection(b1)
add_to_collection(b2)
add_to_collection(b3)

print("======================Train======================")


train1 = Train(101)


train1.validate_id()

train1.display_details()

train1.calculate_fare()


print("\n======================Flight=====================\n")
flight_1 = Flight(1002)

flight_1.validate_id()
flight_1.display_details()
flight_1.calculate_fare()

print("\n======================Flight=====================\n")

bus_1 = Bus(202)

bus_1.validate_id()
bus_1.display_details()
bus_1.calculate_fare()
