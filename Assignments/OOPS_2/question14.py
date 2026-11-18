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
        self.__order = {}
    
    def add_item (self,name,price):
        self.__order[name]= price
        print("item added successfully")
    
    def remove_item(self,name):
        if name in self.__order.keys():
            del self.__order[name]

            print("Item deleted successfully")
        

        else:
            print("Item not found")
    @staticmethod

    def service_tax (self,bill):

        # we are addinfg a service tax as 10 % of the bill : 

        total = self.__bill + (self.__bill /10)
        return total    
    def calcaulate_bill(self):
        sum = 0
        for value in self.__order.values():
            sum+=value
        sum+= Restaurant.service_tax(sum)

        print(f"Your total charges are : {sum}")

    def add_tip(self):
        print("If you want to give the tip to the waiters you can choose the following of the no. here : ")
        print("\n\tPress 1 for yes \n\tPress 2 for no")
        choice = int(input("Enter you choice here  : "))

        if choice == 1:
            print("Please enter the amount of tip you want to give to the waiter here : ")
            tip = int(input("Enter a amount of tip here: "))
            final =self.calcaulate_bill()+tip
            print(f"So after adding a tip for a waiter The final  bill is : {final}")
        
        elif choice ==2:

            print("Ohk dear customer ")
            print("Thanks for comming ")

        else:
            print("You have entered a wrong choice here  : ")

r1 =Restaurant("30")



r1.add_item("Pizza", 250)
r1.add_item("Burger", 150)
r1.add_item("Pasta", 200)
r1.add_item("Cold Coffee", 100)
r1.add_tip()

r1.remove_item("Burger")

r1.calcaulate_bill()


                                                                                                                       