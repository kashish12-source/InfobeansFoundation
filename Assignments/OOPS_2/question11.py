# 11. E-Commerce Product System
# Problem

# Create product system for online store.

# Requirements

# Each product should have:

# product name
# price
# category
# Functionalities
# Apply GST using static method
# Apply category discount
# Display final price
# Concepts Practiced
# static methods
# calculations
# reusable logic

class Product:
    def __init__(self, name, price, category):
        self.__name = name
        self.__price = price
        self.__category = category

    # Static method to calculate GST
    @staticmethod
    def apply_GST(price):
        gst = price * 0.18
        return price + gst

    # Apply category-wise discount
    def discount(self, price):
        if self.__category == "electronics":
            discount = price * 0.10

        elif self.__category == "clothing":
            discount = price * 0.20

        elif self.__category == "food":
            discount = price * 0.05

        else:
            discount = 0

        return price - discount

    # Calculate final price
    def final_price(self):
        price_after_gst = Product.apply_GST(self.__price)

        final = self.discount(price_after_gst)

        print("\nProduct Name:", self.__name)
        print("Category:", self.__category)
        print("Original Price:", self.__price)
        print("Price after GST:", price_after_gst)
        print("Final Price:", final)


# Creating objects

p1 = Product("Laptop", 50000, "electronics")
p2 = Product("Shirt", 2000, "clothing")
p3 = Product("Rice", 1000, "food")

p1.final_price()
p2.final_price()
p3.final_price()
