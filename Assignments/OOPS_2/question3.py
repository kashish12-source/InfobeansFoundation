# 3. Online Shopping Cart
# Problem

# Create a shopping cart system.

# Requirements

# A cart should:

# store customer name
# maintain list of products
# maintain total bill
# Functionalities
# Add product
# Remove product
# Calculate final amount
# Apply discount using static method
# Track total carts created
# Concepts Practiced
# list inside object
# object interaction
# static method
# class variable
class ShoppingMall:
    mall_name ="C21"
    cart_count = 0

    def __init__(self,name):
        ShoppingMall.cart_count +=1
        self.__items = {"chips":20,
        "kurkure":30,
        "maggie":30,
        "ice cream":402,
        "coke":30,
        "oil":475,
        "perfume":4666,
        "floor":75}
        self.__list={}
        self.__name = name 
    
    def add_product(self):
        product_name= input("Enter the name of the product : ")
        product_price = float(input("Enter the price of the product : "))
        if product_name not in self.__items :
            self.__items[product_name] = product_price
            print("Product added successfully")
        else:
            print("Product already exists ")

    def remove_product(self):
        product_name=input("Enter the name of the product you want to  : ")
        if product_name in self.__items:
            del self.__items[product_name]
            print("Deletion of product is successfull")
        else:
            print("Product not found ")

    def add_item(self):
        print("Here are the all products : ")
        for key , value in self.__items.items():
            print(f"{key} : {value}")

        
        item_name = input("Enter item name here : ")
        quantity = int(input("Enter quantity here : "))
        if item_name in self.__items:
            self.__list[item_name]=quantity*(self.__items[item_name])
            print("Product added successfully")

        else:
            print("product not available")
    
    def remove_item(self):
        item_name = input("Enter the item name here : ")
        
        if item_name in self.__list:

            del self.__list[item_name]
            print("Product has been deleted successfully")
        else:
            print("Product not found ")

    @staticmethod
    def discount(balance):
        if balance >2000:
            
            total = balance - balance*(10/100)
            return total
        elif balance <1000:
            total = balance - balance*(5/100)
            return total
        else:
            return 0


    def calculate_bill (self):
        amount = 0
        for value in self.__list.values():
            amount+=value
        print(f"Total bill is : {amount}")
        print(f"Bill after discount is : {ShoppingMall.discount(amount)}")
    @classmethod
    def total_cart_created (cls):
        print(f"The total cart created is : {ShoppingMall.cart_count}")


c1 = ShoppingMall("kashish")
c2=ShoppingMall("keshav")
c3 = ShoppingMall("piyush")
c4 = ShoppingMall("kartavya")

c1.add_item()
# c1.add_item()
# c1.add_item()
c1.calculate_bill()

ShoppingMall.total_cart_created()

# c2.add_item()
# c2.add_item()
# c2.add_item()
# c2.calculate_bill()





