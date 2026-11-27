# 41. Cab Booking Application

# Features:

# User booking
# Driver assignment
# Fare calculation

# Use:

# inheritance
# abstraction
# polymorphism


from abc import ABC ,abstractmethod

class DistanceCannotBeZeroError(Exception):
    pass 

class Booking(ABC):
    cabs_available = 100
    def __init__(self,cab_no,driver_name,price):
        # here cab_no = vehicle no and price means price / km
        self.__cab_no = cab_no
        self.__driver_name = driver_name
        self.__price = price 

    def avail_cabs():
        return Booking.cabs_available
    
    def get_details(self):
        return self.__cab_no,self.__driver_name

    def get_price(self):
        return self.__price
    @abstractmethod
    def calculate_fare(self):
        pass 
    
    @abstractmethod
    def display_details(self):
        pass 
    
class User(Booking):
    __fare = 0
    is_book = False
    def calculate_fare(self):

        avail = Booking.avail_cabs()
        
        try:
            if avail > 0:
                no_of_cab = int(input("Enter the no. of cabs you want to book : "))
                if 0<no_of_cab <= avail:
                    Booking.cabs_available -=no_of_cab
                    print("The booking of the cabs are possible")
                    distance = float(input("Enter the distance you want to travle : "))
                    if distance<= 0:
                        raise DistanceCannotBeZeroError
                    
                    price = self.get_price()
                    User.__fare = price * distance

                    Booking.cabs_available -= no_of_cab
                    User.is_book = True  
        except DistanceCannotBeZeroError as e:
            print("You have to travel a distance to book a cab, so the distance cannot be zero")
        
        finally :
            if User.is_book:
                print("Thank you for booking the cab happy journey ")
            else:
                print("Thank you ")
    def display_details(self):
        if User.is_book:
            cab_no, driver_name = self.get_details()
            print(f"===============================Ride Details=============================")
            print(f"Name of the drive -> {driver_name}")
            print(f"Cab number is -> {cab_no}")
            print(f"The fare of the journey is -> {User.__fare}")
            print("===============================Happy Journey=============================")
        else:
            print("No ride is booked ")



user1 = User("MP09AB1234", "Rahul", 15)
user2 = User("MP09CD5678", "Aman", 20)

user1.calculate_fare()
user1.display_details()

user2.calculate_fare()
user2.display_details()