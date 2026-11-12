
# 16. Train Reservation System
# Problem

# Design ticket reservation system.

# Requirements

# Train should contain:

# train number
# total seats
# booked seats
# Functionalities
# Reserve seat
# Cancel seat
# Display available seats

class Train:
    def __init__(self, train_no, total_seats):
        self.__train_no = train_no
        self.__total_seats = total_seats
        self.__booked_seats = 0

    def reserve_seat(self):
        if self.__booked_seats < self.__total_seats:
            self.__booked_seats += 1
            print("Seat reserved successfully")
        else:
            print("Sorry! No seats available")

    def cancel_seat(self):
        if self.__booked_seats > 0:
            self.__booked_seats -= 1
            print("Seat cancelled successfully")
        else:
            print("No booked seats available to cancel")

    def display_seats(self):
        available = self.__total_seats - self.__booked_seats

        print("\nTrain Number:", self.__train_no)
        print("Total Seats:", self.__total_seats)
        print("Booked Seats:", self.__booked_seats)
        print("Available Seats:", available)

t1 = Train(12345, 5)
t2 = Train(67890, 3)

print("Train 12345")

t1.reserve_seat()
t1.reserve_seat()
t1.reserve_seat()

t1.display_seats()

print("\nCancelling a seat")

t1.cancel_seat()

t1.display_seats()
print("\nTrain 67890")

t2.reserve_seat()
t2.display_seats()
