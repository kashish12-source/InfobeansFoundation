# 14. Restaurant Billing System
# Problem

# Create restaurant order system.

# Requirements

# Each order:

# table number
# ordered items
# prices
# Functionalities
# Add items
# Remove items
# Calculate total bill
# Add service tax using static method



class Restaurant:
    def __init__(self, table_no):
        self.__table_no = table_no
        self.__ordered_items = {}

    def add_items(self, item, price):
        self.__ordered_items[item] = price
        print(item, "added successfully")

    def remove_items(self, item):
        if item in self.__ordered_items:
            del self.__ordered_items[item]
            print(item, "removed successfully")
        else:
            print("Item not found")

    def total_bill(self):
        total = 0

        print("\nTable Number:", self.__table_no)
        print("\nOrdered Items:")

        for item, price in self.__ordered_items.items():
            print(item, ":", price)
            total += price

        print("Total amount:", total)

        final = Restaurant.service_tax(total)

        print("Service Tax (5%):", total * 0.05)
        print("Final Bill:", final)

    @staticmethod
    def service_tax(amount):
        tax = amount * 0.05
        return amount + tax


r1 = Restaurant(101)


r1.add_items("Pizza", 250)
r1.add_items("Burger", 150)
r1.add_items("Pasta", 200)
r1.add_items("Cold Coffee", 100)

r1.remove_items("Burger")


r1.total_bill()
