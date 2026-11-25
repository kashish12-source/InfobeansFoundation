# 24. ATM System

# Abstract:

# ATM

# Derived:

# SBIATM
# HDFCATM

# Implement banking operations.


from abc import ABC ,abstractmethod

class ATM(ABC):

    @abstractmethod
    def check_pin(self):
        pass
    
    @abstractmethod
    def check_balance(self):
        pass 

    @abstractmethod
    def check_bank(self):
        pass 



collection = []
def add_to_collection(obj):
    collection.append(obj)

class Customer :

    def __init__(self,name,bank,pin,balance):
        self.__name = name 
        self.__bank = bank
        self.__pin = pin 
        self.__balance = balance
        self.__valid_bank = False
        self.__valid_pin = False
    
    def get_bank(self):
        return self.__bank
    
    def get_pin(self):
        return self.__pin
    
    def get_balance(self):
        return self.__balance
    

class SBI(ATM):
    def __init__(self, pin,bank,amount):
        self.__pin = pin
        self.__bank  = bank
        self.__amount = amount
        self.__valid_bank = False
        self.__valid_pin = False 

    def check_bank(self):
        for obj in collection:
            if obj.get_bank() == self.__bank :
                self.__valid_bank = True
                print("Bank is valid ")
            
                return True
        print("Bank is not valid ")
        return False
    
    def check_pin(self):
        for obj in collection:
            if obj.get_pin() == self.__pin:
                self.__valid_pin = True
                print("Pin is valid")
                return True
        print("Pin is not is valid ")
        return False
    
    def check_balance(self):
        if self.__valid_bank and self.__valid_pin:
            for obj in collection:
                if obj.get_balance() >= self.__amount:
                    print("Transaction is possible")
        else:
            print("Transaction is not possible")



class HDFC(ATM):
    def __init__(self, pin,bank,amount):
        self.__pin = pin
        self.__bank  = bank
        self.__amount = amount
        self.__valid_bank = False
        self.__valid_pin = False 

    def check_bank(self):
        for obj in collection:
            if obj.get_bank() == self.__bank :
                self.__valid_bank = True
                print("Bank is valid ")
            
                return True
        print("Bank is not valid ")
        return False
    
    def check_pin(self):
        for obj in collection:
            if obj.get_pin() == self.__pin:
                self.__valid_pin = True
                print("Pin is valid")
                return True
        print("Pin is not is valid ")
        return False
    
    def check_balance(self):
        if self.__valid_bank and self.__valid_pin:
            for obj in collection:
                if obj.get_balance() >= self.__amount:
                    print("Transaction is possible")
        else:
            print("Transaction is not possible")


# Creating customers

c1 = Customer("Kashish", "SBI", 1234, 10000)
c2 = Customer("Koshiki", "HDFC", 5678, 15000)

# Adding customers to collection

add_to_collection(c1)
add_to_collection(c2)


# Creating SBI ATM object

s = SBI(1234, "SBI", 2000)

print("\n----- SBI ATM -----")

s.check_bank()
s.check_pin()
s.check_balance()


# Creating HDFC ATM object

h = HDFC(5678, "HDFC", 5000)

print("\n----- HDFC ATM -----")

h.check_bank()
h.check_pin()
h.check_balance()

