# 19. Flight Reservation System
# Problem

# Create airline reservation software.

# Requirements

# Flight should contain:

# flight number
# total seats
# booked seats
# Functionalities
# Book ticket
# Cancel ticket
# Prevent overbooking


class Flight:
    def __init__(self, flight_no, total_seats):
        self.__flight_no = flight_no
        self.__total_seats = total_seats
        self.__booked_seats = 0

    def book_ticket(self):
        if self.__booked_seats < self.__total_seats:
            self.__booked_seats += 1
            print("Ticket booked successfully")

        else:
            print("Sorry! No seats available")

    def cancel_ticket(self):
        if self.__booked_seats > 0:
            self.__booked_seats -= 1
            print("Ticket cancelled successfully")

        else:
            print("No booked tickets available to cancel")

    def display_details(self):
        available = self.__total_seats - self.__booked_seats

        print("\nFlight Number:", self.__flight_no)
        print("Total Seats:", self.__total_seats)
        print("Booked Seats:", self.__booked_seats)
        print("Available Seats:", available)

f1 = Flight(101, 5)
f2 = Flight(102, 3)

print("Flight 101")

f1.book_ticket()
f1.book_ticket()
f1.book_ticket()

f1.display_details()

print("\nCancelling ticket")
f1.cancel_ticket()

f1.display_details()
print("\nTesting Flight 102")

f2.book_ticket()
f2.book_ticket()
f2.book_ticket()
f2.book_ticket()

f2.display_details()
