# 13. Write a Java program to create a class called "Inventory" with a collection of products and methods to add and remove products, and to check for low inventory.

class Inventory:
    def __init__(self):
        self.collection ={}

    def add_product(self,product,quantity=1):
        if product in self.collection:
            self.collection[product] +=quantity
        else:
            self.collection[product]=quantity

    def remove_product(self,product ,quantity=1):
        if product in self.collection:
            if self.collection[product]<quantity:
                print("The quantity is not available")
            else:
                self.collection[product] -=quantity
                print(f"Now only these peaces are left : {self.collection[product]}")
        else:
            print("Product not found ")
    def display_collection(self):
        for key,value in self.collection.items():
            print(f"{key} : {value}")

p1 = Inventory()
p1.add_product("laptop",20)
p1.add_product("keyboard")
p1.add_product("cpu",30)
p1.add_product("GPU",3)
p1.display_collection()
p1.remove_product("keyboard",1)
p1.display_collection()
