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
    __cars ={}

    def __init__(self, no, model,price ,no_cars):
        self.__no = no
        self.__model = model
        self.__price = price 
        self.__no_cars = no_cars
        CarRental.__cars[self.__no] = {"model" :self.__model, "price ":self.__price,"available":self.__no_cars}



    def rent_car(self):
        if self.__no in CarRental.__cars:
            count = int(input("Enter the no. of cars you want to take for rent : "))
            if count < CarRental.__cars[self.__no]["available"]:
                CarRental.__cars[self.__no]["available"]-=count
                print("Car has been rented successfully")
            else:
                print("This much cars are not avaiable")
                return 
        else:
            print("Car not found")
            return

        
    def return_car(self):
        if self.__no in CarRental.__cars:
            count = int(input("Enter the no. of cars you want to return "))

            CarRental.__cars[self.__no]["available"] += count
            print("Car has been returend successfully")
        else:
            print("Car not found ")


    def calculat_rent(self):
        days = int(input("\nEnter the no. of days you have rented the car"))
        total = days * self.__price
        print(f"Your total bill is : {total}")
    




c1 = CarRental(101, "BMW", 5000, 5)
c2 = CarRental(102, "Thar", 3000, 28)
c3 = CarRental(103, "Swift", 1500, 24)

print("Renting BMW")
c1.rent_car()

print("\nCalculating rental amount")
c1.calculat_rent()

print("\nReturning BMW")
c1.return_car()

print("\nRenting Swift")
c3.rent_car()



