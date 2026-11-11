
class MovieTicket:

    total_seats = 150

    def __init__(self, name, available_seats):
        self.__name = name
        self.__total = available_seats
        self.__available_seats = available_seats
        self.__booked_seats = 0

    def Book_ticket(self):

        movie_name = input("Enter the name of the movie here: ")
        no_of_ticket = int(input("Enter the number of tickets you want: "))

        if movie_name == self.__name:

            if no_of_ticket > 0 and no_of_ticket <= self.__available_seats:

                self.__available_seats -= no_of_ticket
                self.__booked_seats += no_of_ticket

                print("Your tickets have been booked successfully")

            else:
                print("Booking not possible. Seats unavailable")

        else:
            print("Movie not found")

    def Cancel_ticket(self):

        movie_name = input("Enter the name of the movie: ")

        if movie_name == self.__name:

            no_of_ticket = int(input("Enter the number of tickets to cancel: "))

            if no_of_ticket > 0 and no_of_ticket <= self.__booked_seats:

                self.__available_seats += no_of_ticket
                self.__booked_seats -= no_of_ticket

                print("Your tickets have been cancelled successfully")

            else:
                print("Ticket cancellation is not possible")

        else:
            print("Movie not found")

    def display_availability(self):

        print(f"Movie name: {self.__name}")
        print(f"Total seats: {self.__total}")
        print(f"Available seats: {self.__available_seats}")
        print(f"Booked seats: {self.__booked_seats}")


m1 = MovieTicket("dhurandar", 60)
m2 = MovieTicket("shiddat", 75)

m1.display_availability()
m1.Book_ticket()
m1.Cancel_ticket()
m1.display_availability()

m2.display_availability()
