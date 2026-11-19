'''
Movie ticket booking
parent - ticket
derived - gold ticket , platinum ticket , vip ticket
apply pricing logic
'''

from abc import ABC, abstractmethod

class Ticket(ABC):
    @abstractmethod
    def display_available(self):
        pass 

    @abstractmethod
    def booking(self):
        pass 
    
    @abstractmethod
    def canceling(self):
        pass

    __seats_available = {}
    __movies=[]
    def seats_available(self):
        Ticket.__movies = ["dhurandar","shiddat","ddlj","hanuman ansh"]
        for name in Ticket.__movies:
            Ticket.__seats_available[name] = 50


 

class Gold_Ticket(Ticket):
    __platform_charges = 100
    
    __seats_available= {"dhurandar":50,"shiddat":50,"ddlj":230,"hanuman ansh":500}


    def display_available(self):
        
        for key , val in Gold_Ticket.__seats_available.items():
            print(f"{key} : {val}")
        
    def booking(self):
        name = input("Enter the name of the movie you want to book for : ")
        if name in Gold_Ticket.__seats_available:
            quantity = int(input("Enter the no. of ticket you want to purchase : "))
            if quantity < Gold_Ticket.__seats_available[name]:
                Gold_Ticket.__seats_available[name] -=quantity
                print("Your tickets has been booked successfully")
                bill = quantity * 300
                if bill > 1200:
                    bill = bill- (bill/10) + Gold_Ticket.__platform_charges
                    print(f"Your bill is : {bill}")
                elif bill <=1200 and bill >600:
                    bill = bill - (bill/0.05) + Gold_Ticket.__platform_charges

                    print(f"Your bill is : {bill}")
                else:
                    print(f"Your bill is : {bill + Gold_Ticket.__platform_charges}")

                
                
            else:
                print("We don't have this much movie tickets right now ")

        else:
            print("Movie is not their")
        
        
    def canceling(self):
        name = input("Enter the name of the moive you want to cancel ticket of : ")
        if name in Gold_Ticket.__seats_available:
            quantity = int(input("Enter th quantity of the tickets you want to cancel : "))
            sold_tickets = 50 - Gold_Ticket.__seats_available[name]
            
            if 0< quantity <= sold_tickets:
                Gold_Ticket.__seats_available[name]+=quantity
                print("Your ticket has been cancelled successfully")
                bill = quantity *300
                if bill > 1200:
                    bill = bill *0.5

                    print(f"amount that is returned is : {bill}")
                elif bill <=1200 and bill >600:
                    bill = bill *0.75
                    print(f"amount that is returned is : {bill}")
                else:
                    print(f"amount that is returned is : {bill}")
            else:
                print("This much quantity of tickets have not been sold")
        else:
            print("The movie is not their in the theater")
    
    
g1 = Gold_Ticket()

g1.display_available()

g1.booking()

g1.canceling()

g2 = Gold_Ticket()

g2.display_available()

g2.booking()

g2.canceling()





        

    


