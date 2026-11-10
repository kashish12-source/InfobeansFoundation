# 19. Write a Java program to create a class with methods to search for flights and hotels, and to book and cancel reservations.
class TripPlanner:
    def __init__(self):
        self.__flights= {"indigo":7,"air india":8}
        self.__hotels = {"marriot":9,"radisson":30}
    
    def search_flights(self):
        for key , val in self.__flights.items():
            if key !=0:
                print(f"flight name : {key}")
                print(f"seats available is : {val}")
    
    def search_hotels(self):
        for key , val in self.__hotels.items():
            if key !=0:
                print(f"hotel name : {key}")
                print(f"rooms available is : {val}")
    
    def book_flight(self):
        name = input("Enter the name of the flight")
        if name in self.__flights:

            seats = int(input("Enter the no. of seats you have to book : "))
            if seats <self.__flights[name] and seats>0:
                self.__flights[name] -=seats
                print("Your booking is confirmed")
            else:
                print("This much seats are not available in the flight ")
        else:
            print("The flight name not found")

    def book_hotel(self):
        name = input("Enter the name of the hotel")
        if name in self.__hotels:

            rooms = int(input("Enter the no. of rooms you have to book : "))
            if rooms <self.__hotels[name]:
                self.__hotels[name] -=rooms
                print("Your booking is confirmed")
            else:
                print("This much rooms are not available in the hotel ")
        else:
            print("The hotel name not found")

    def cancel_flight(self):
        name = input("Enter the flight name: ").lower()

        if name in self.__flight_bookings:
            seats = int(input("Enter the number of seats to cancel: "))

            if 0 < seats <= self.__flight_bookings[name]:

                self.__flights[name] += seats

                self.__flight_bookings[name] -= seats

                print("Flight cancellation successful")

            else:
                print("Invalid cancellation request")

        else:
            print("No booking found for this flight")

            
    def cancel_hotel(self):
        name = input("Enter the hotel name: ").lower()

        if name in self.__hotel_bookings:
            rooms = int(input("Enter the number of rooms to cancel: "))

            if 0 < rooms <= self.__hotel_bookings[name]:
                self.__hotels[name] += rooms
                self.__hotel_bookings[name] -= rooms

                print("Hotel cancellation successful!")

            else:
                print("Invalid cancellation request!")

        else:
            print("No booking found for this hotel!")

c1 = TripPlanner()
c1.search_hotels()
c1.book_hotel()
c1.search_flights()
c1.book_flight()
c1.search_flights()
c1.search_hotels()
