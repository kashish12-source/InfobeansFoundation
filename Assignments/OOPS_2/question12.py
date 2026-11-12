# 12. Car Rental System
# Problem

# Create a car rental platform.

# Requirements

# Each car:

# car number
# model
# rental price per day
# availability
# Functionalities
# Rent car
# Return car
# Calculate rent amount
# Prevent renting unavailable cars

class CarRental:
    def __init__(self, no, model, price, availability):
        self.__no = no
        self.__model = model
        self.__price = price
        self.__availability = availability

    def rent_car(self):
        if self.__availability == True:
            self.__availability = False
            print(f"{self.__model} has been rented successfully")

        else:
            print("Sorry! Car is not available")

    def return_car(self):
        if self.__availability == False:
            self.__availability = True
            print(f"{self.__model} has been returned successfully")

        else:
            print("This car was not rented")

    def amount(self):
        if self.__availability == False:
            days = int(input("Enter number of rental days: "))

            if days > 0:
                total = days * self.__price
                print("Car:", self.__model)
                print("Rental days:", days)
                print("Total rental amount:", total)

            else:
                print("Enter valid rental days")

        else:
            print("Please rent the car first")



c1 = CarRental(101, "BMW", 5000, True)
c2 = CarRental(102, "Thar", 3000, True)
c3 = CarRental(103, "Swift", 1500, False)

print("Renting BMW")
c1.rent_car()

print("\nCalculating rental amount")
c1.amount()

print("\nReturning BMW")
c1.return_car()

print("\nRenting Swift")
c3.rent_car()
