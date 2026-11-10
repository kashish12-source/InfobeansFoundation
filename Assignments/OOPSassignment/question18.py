# 18. Write a Java program to create a class called "Restaurant" with attributes for menu items, prices, and ratings, and methods to add and remove items, and to calculate average rating.
import dis
class Restaurant:
    def __init__(self, *ratings):
        self.__ratings = list(ratings)
        self.__menu = ["pizza","pasta","manchurian"]
        self.__price = {"pizza":120,"pasta":140,"manchurian":230}
    
    def add_items (self):
        item_name = input("Enter the name of the item here : ")
        item_price = float(input("Enter the price of the item here : "))
        if item_name not in self.__price:
            self.__price[item_name]= item_price
        else:
            print("The item is already in the menu ")
            return
        if item_name not in self.__menu:
            self.__menu.append(item_name)
            print("Item added successfully ")

        else:
            print("The item is already in the menue")
    
    def remove_items(self):
        item_name = input("Enter the name of the item here : ")
        if item_name in self.__menu:
            self.__menu.remove(item_name)
            if item_name in self.__price:
                del self.__price[item_name]
                print("The item has been deleted successfully")
                return
        else:
            print("The item not found")
    
    def calculate_average(self):
        if len(self.__ratings)==0:
            return 0
        average = sum(self.__ratings)/len(self.__ratings)
        return average
    def display_menu(self):
        for i in self.__menu:
            print(i)


    
custormer_1 = Restaurant(2,4,4,7)
average = custormer_1.calculate_average()

print(average)
print("Removing element form the menu")
print("menu before deletion")
custormer_1.display_menu()

custormer_1.remove_items()
print("menue after deletion")
custormer_1.display_menu()


print()
print("Adding items in the menue")
print("menu befor adding item")
custormer_1.display_menu()
custormer_1.add_items()
print("\nmenu after adding item")
custormer_1.display_menu()







            
        




