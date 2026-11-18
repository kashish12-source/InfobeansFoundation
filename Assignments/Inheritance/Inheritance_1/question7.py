# 7. Shopping Cart System

# Base:

# Product

# Derived:

# Electronics
# Grocery
# Clothing

# Apply discounts.

from abc import ABC,abstractmethod
class Product(ABC):

    @abstractmethod
    def add_product(self):
        pass

    @abstractmethod
    def calculate_bill(self):
        pass 

    @abstractmethod
    def discount(self):
        pass 

class Grocery(Product):
    def __init__(self):
        self.__collection = {"paneer":30,
        "potato" :20,
        "tomato":40,
        "sauce":50,
        "chilli":30,
        "soyabean":704}
        self.__product={}

    def display_grocery(self):
        for key ,val in self.__collection.items():
            print(f"{key} = {val} rupees")
    
    def add_product(self):
        while(True):
            print("Press 1 to add product\nPress 2 if you are done with adding product")
            choice = int(input("Enter your choice here : "))
            if choice == 1:
                name = input("Enter the name of the product here : ")

                if name in self.__collection:
                    quantity = int(input("Enter the quantity here : "))
                    self.__product[name] = quantity*self.__collection[name]
                else:
                    print("The product not found ")
            elif choice == 2:
                
                break
            else:
                print("Enter the valid choice please ")

    def calculate_bill(self):
        bill = 0
        for val in self.__product.values():
            bill +=val
        print(f"Your bill is : {bill}")
        
        return bill
    
    def discount(self):
        amount = self.calculate_bill()

        if amount >=10000:
            discount = amount - amount/10
            print(f"Your final bill is : {discount}")
            return 
        elif amount >= 5000 and amount<1000:
            discount = amount - amount*0.05
            print(f"Your final bill is : {discount}")
        else:
            print("You Don't meet any of the condition hence you don't get any discount")




            
class Clothing(Product):
    def __init__(self):
        self.__collection={
            "jeans":6400,
            "pants":700,
            "trouser":1200,
            "skirt":1500,
            "top" :450,
            "kurti":500,
            "crops":3000
        }
        self.__product={}
    
    def display(self):
        for key ,val in self.__collection.items():
            print(f"{key} = {val} rupees")
    
    def add_product(self):
        while(True):
            print("Press 1 to add product\nPress 2 if you are done with adding product")
            choice = int(input("Enter your choice here : "))
            if choice == 1:
                name = input("Enter the name of the product here : ")

                if name in self.__collection:
                    quantity = int(input("Enter the quantity here : "))
                    self.__product[name] = quantity*self.__collection[name]
                else:
                    print("The product not found ")
            elif choice == 2:
                
                break
            else:
                print("Enter the valid choice please ")

    def calculate_bill(self):
        bill = 0
        for val in self.__product.values():
            bill+=val
        print(f"Your bill is : {bill}")

        return bill

    def discount(self):
        amount = self.calculate_bill()
        if amount >=10000:
            discount = amount - amount/10
            print(f"Your final bill is : {discount}")
            return 
        elif amount >= 5000 and amount<1000:
            discount = amount - amount*0.05
            print(f"Your final bill is : {discount}")
        else:
            print("You Don't meet any of the condition hence you don't get any discount")


        


class Electronics(Product):
    
    def __init__(self):
        self.__Collection = {"plug":23,
        "pin":436,
        "switch" :56,
        "wire":643,
        "rod":36
        }
        self.__products = {}
    
    def display_products(self):
        for key,val in self.__Collection.items():
            print(f"{key} = {val}rupees")

    def add_product(self):
            
            while(True):
                print("Press 1 to add the product \nPress 2 stop it ")
                choice = int(input("Enter you choice here : "))
                
                if choice==1:
                    name = input("Enter the name of the product : ")
                    if name in self.__Collection:
                        quant = int(input("Enter the quantity of the product here : "))
                        self.__products[name] = quant*self.__Collection[name]

                    else :
                        print("Product not found")
                elif choice ==2 :
                    
                    break
                else :
                    print("Please enter the valid choice ")


    def calculate_bill(self):
        bill = 0
        for val in self.__products.values():
            bill+=val
        
        print(f"Your bill is : {bill}")
        return bill
    
    def discount(self):
        amount = self.calculate_bill()
        if amount >=10000:
            discount = amount - amount/10
            print(f"Your final bill is : {discount}")
            return 
        elif amount >= 5000 and amount<1000:
            discount = amount - amount*0.05
            print(f"Your final bill is : {discount}")
        else:
            print("You Don't meet any of the condition hence you don't get any discount")

print("\nProduct of Electronics\n")
e1 = Electronics()
e1.display_products()
e1.add_product()
e1.discount()

print("\nProduct of Clothings\n ")
c1 = Clothing()
c1.display()
c1.add_product()
c1.discount()

print("\nProduct of Grocery\n")
g1 = Grocery()
g1.display_grocery()
g1.add_product()
g1.discount()








