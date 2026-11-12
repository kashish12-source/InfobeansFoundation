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
    def __init__(self, name, price , category ):
        self.__name = name 
        self.__price = price 
        self.__category = category 

    @staticmethod
    def add_gst(price):
        gst = price *0.18
        return price +gst
    
    def category_discount(self):
        if self.__category.lower() == "electronics":
            discount = self.__price *0.2
            return self.__price - discount
        elif self.__category.lower() == "food":
            discount = self.__price *0.3
            return self.__price - discount

        elif self.__category.lower() == "clothing":
            discount = self.__price *0.1
            return self.__price -discount
        else:
            
            print("no discount")
            return self.__price
    
    def final_price(self):
        discount = self.category_discount()
        gst = Product.add_gst(discount)
        print(f"Final price of the product is : {gst}")


p1 = Product("Laptop", 50000, "electronics")
p2 = Product("Shirt", 2000, "clothing")
p3 = Product("Rice", 1000, "food")
p4 = Product("car", 5673,"toy")

p1.final_price()
p2.final_price()
p3.final_price()
p4.final_price()








