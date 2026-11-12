# 17. Electricity Bill System
# Problem

# Generate electricity bill.

# Requirements

# Consumer should contain:

# consumer id
# units consumed
# Functionalities
# Calculate bill
# Add surcharge using static method
# Display bill summary


class ElectricityBill:
    def __init__(self, consumer_id, units):
        self.__consumer_id = consumer_id
        self.__units = units

    def calculate_bill(self):
        if self.__units <= 100:
            bill = self.__units * 3

        elif self.__units <= 200:
            bill = (100 * 3) + ((self.__units - 100) * 5)

        elif self.__units <= 300:
            bill = (100 * 3) + (100 * 5) + ((self.__units - 200) * 7)

        else:
            bill = (100 * 3) + (100 * 5) + (100 * 7) + ((self.__units - 300) * 10)

        return bill

    @staticmethod
    def add_surcharge(amount):
        surcharge = amount * 0.05
        return amount + surcharge

    def display_bill(self):
        if self.__units < 0:
            print("Invalid units consumed")
            return

        bill = self.calculate_bill()
        final_bill = ElectricityBill.add_surcharge(bill)

        print("\n------ ELECTRICITY BILL ------")
        print("Consumer ID:", self.__consumer_id)
        print("Units Consumed:", self.__units)
        print("Electricity Charges:", bill)
        print("Surcharge (5%):", bill * 0.05)
        print("Final Bill:", final_bill)

c1 = ElectricityBill(101, 150)
c2 = ElectricityBill(102, 250)
c3 = ElectricityBill(103, 350)
c1.display_bill()
c2.display_bill()
c3.display_bill()
