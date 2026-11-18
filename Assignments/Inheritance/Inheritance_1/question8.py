'''
oline Food Delivery
parent - Food Items
chiled = pizza burger and sandwich 
calcutate total bill


'''
from abc import ABC ,abstractmethod
class FoodItems(ABC):
    @abstractmethod
    def products(self):
        pass 

    @abstractmethod
    def calculate_bill(self):
        pass 

class Pizza(FoodItems):
    def __init__(self):
        self.__collection={
            "capsicum":120,
            "onion":230,
            "corn":140,
            "corn and capsicum":230,
            "cheese corn":210
        }
        self.__product = {}
    def dispaly(self):
        for key ,val in self.__collection.items():
            print(f"{key} : {val}")
        
    
    def products(self):
        while(True):
            print("Press 1 to add the pizza in your cart \nPress 2 if you are done with all the stuff ")
            choice = int(input("Enter you choice here : "))
            if choice == 1:
                name = input("Enter name of the pizza here : ")
                if name in self.__collection:
                    quantity = int(input("Enter the no. of pizza you need "))
                    self.__product[name] = quantity * self.__collection[name]
                else:
                    print("Product not avialable")
            elif choice == 2:
                break
            else:
                print("Please enter a valid choice ")
    def calculate_bill(self):
        bill = 0
        for val in self.__product.values():
            bill +=val
        print("____________WELCOME TO DOMINOS_____________")
        for key ,val in self.__product.items():
            print(f"{key} : {val}")
        print(f"\nYour final bill is : {bill}")
        print("_____________HAVE A NICE DAY________________")

class Burger(FoodItems):
    def __init__(self):
        self.__collection={
            "aloo tikki burger":60,
            "cabage burger":80,
            "cheese burger":120

        }
        self.__product = {}
    
    def products(self):
        while(True):
            print("Press 1 to add the burger in your cart \nPress 2 if you are done with all the stuff ")
            choice = int(input("Enter you choice here : "))
            if choice == 1:
                name = input("Enter name of the burger here : ")
                if name in self.__collection:
                    quantity = int(input("Enter the no. of pizza you need "))
                    self.__product[name] = quantity * self.__collection[name]
                else:
                    print("Product not avialable")
            elif choice == 2:
                break
            else:
                print("Please enter a valid choice ")
    def display(self):
        for key , val in self.__collection.items():
            print(f"{key} : {val}")
    
    def calculate_bill(self):
        bill = 0
        for val in self.__product.values():
            bill +=val
        print("____________WELCOME TO BURGER KING_____________")

        for key ,val in self.__product.items():
            print(f"{key} : {val}")
        print(f"\nYour final bill is : {bill}")
        print("_____________HAVE A NICE DAY________________")

class Sandwich(FoodItems):
    def __init__(self):
        self.__collection={
            "plain sandwich":60,
            "chutney sandwich":80,
            "cheese sandwich":120,
            "paneer sandwich":140,
            "jain sandwich":50,
            "jam sandwich":60

        }
        self.__product = {}
    
    def products(self):
        while(True):
            print("Press 1 to add the burger in your cart \nPress 2 if you are done with all the stuff ")
            choice = int(input("Enter you choice here : "))
            if choice == 1:
                name = input("Enter name of the Burger here : ")
                if name in self.__collection:
                    quantity = int(input("Enter the no. of burger you need "))
                    self.__product[name] = quantity * self.__collection[name]
                else:
                    print("Product not avialable")
            elif choice == 2:
                break
            else:
                print("Please enter a valid choice ")
    def display(self):
        for key , val in self.__collection.items():
            print(f"{key} : {val}")
    
    def calculate_bill(self):
        bill = 0
        for val in self.__product.values():
            bill +=val
        print("____________WELCOME TO NAMO SANDWICH_____________")

        for key ,val in self.__product.items():
            print(f"{key} : {val}")
        print(f"\nYour final bill is : {bill}")
        print("_____________HAVE A NICE DAY________________")
print("\nNow we have to choose the sandwich here \n")
s1 = Sandwich()      
s1.display()
s1.products()
s1.calculate_bill()
print("\nNow we have to choose the pizza here \n")
p1 = Pizza()
p1.dispaly()
p1.products()
p1.calculate_bill()
print("\nNow we have to choose the burger here \n")
b = Burger()
b.display()
b.products()
b.calculate_bill()

            



















