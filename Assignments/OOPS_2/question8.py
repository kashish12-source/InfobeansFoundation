# 8. Inventory Management System
# Problem

# Create product inventory software.

# Requirements

# Each product should contain:

# product id
# product name
# quantity
# price
# Functionalities
# Add stock
# Reduce stock after purchase
# Prevent negative stock
# Calculate inventory value
# Concepts Practiced
# arithmetic inside classes
# validations
# inventory logic

class Inventory:

    __data = {}
    bill = 0

    def __init__(self, product_id, name, quantity, price):

        self.__product_id = product_id
        self.__name = name
        self.__quantity = quantity
        self.__price = price

        Inventory.__data[self.__product_id] = {
            "name": self.__name,
            "quantity": self.__quantity,
            "price": self.__price
        }

    def add_stock(self):

        id = int(input("Enter the product id: "))

        if id in Inventory.__data:

            stock = int(input("Enter the stock here: "))

            if stock > 0:
                Inventory.__data[id]["quantity"] += stock
                print("Stock added successfully")
            else:
                print("Enter a valid quantity")

        else:
            print("Product not found")

    def purchase(self):

        id = int(input("Enter the product id: "))

        if id in Inventory.__data:

            stock = int(input("Enter the amount you want to purchase: "))

            if stock > 0 and stock <= Inventory.__data[id]["quantity"]:

                Inventory.__data[id]["quantity"] -= stock

                Inventory.bill += stock * Inventory.__data[id]["price"]

                print("Product purchased successfully")
                print(f"Your bill is: {Inventory.bill}")

            else:
                print("Not enough stock or invalid quantity")

        else:
            print("Product not found")

    def inventory_value(self):

        total = 0

        for key, value in Inventory.__data.items():

            total += value["quantity"] * value["price"]

        print(f"Total inventory value: {total}")


# Creating objects

p1 = Inventory(101, "Laptop", 10, 50000)
p2 = Inventory(102, "Mouse", 20, 500)

p1.add_stock()
p1.purchase()
p1.inventory_value()
