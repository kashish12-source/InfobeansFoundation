# 5. Banking System

# Parent:

# BankAccount

# Child:

# SavingsAccount
# CurrentAccount

# Implement withdrawal rules.

from abc import ABC , abstractmethod
class BankAccount(ABC):
    @abstractmethod
    def details(self):
        pass 
    @abstractmethod
    def withdraw(self):
        pass 

    @abstractmethod
    def deposite(self):
        pass 
class SavingsAccount(BankAccount):
    
    def __init__(self, name ,age ,contact ,amount):
        self.__name = name 
        self.__age = age 
        self.__contact = contact
        self.__amount = amount 
        self.__ifsc = "SBI"
    
    @staticmethod
    def withdraw_limits():
        return 10000
    
    @staticmethod
    def deposite_limits():
        return 20000


    def details(self):
        print(f"_______________________BRANCH - {self.__ifsc}_____________________")
        print(f"Name : {self.__name}")
        print(f"Age : {self.__age}")
        print(f"Contact : {self.__contact}")
        print(f"Balance : {self.__amount}")
        print("____________________________________________________________________")
    
    def withdraw(self):
        withdraw_amount = float(input("Enter the withdraw amount here : "))
        if withdraw_amount < self.__amount and withdraw_amount<SavingsAccount.withdraw_limits():
            self.__amount -=withdraw_amount
            print(f"Balance deducted successfully\nBalance left is : {self.__amount}\n")
        elif withdraw_amount>SavingsAccount.limits():
            print("This much amount withdrawling is not possible in savings account as a single transaction")
        else:
            print("Your balance is not enough")

    def deposite(self):
        deposite_amount = float (input("Enter the amount you want to deposite in the account here : "))
        if deposite_amount <= SavingsAccount.deposite_limits():
            self.__amount+=deposite_amount
            print(f"Amount deposited successfully\nNow the balance is : {self.__amount}")
        else:
            print("Such a big tansaction is not possible in the savings account")
        
class CurrentAccount(BankAccount):
    def __init__(self, name ,age ,contact ,amount):
        self.__name = name 
        self.__age = age 
        self.__contact = contact
        self.__amount = amount 
        self.__ifsc = "SBI"
    

    def details(self):
        print(f"_______________________BRANCH - {self.__ifsc}_____________________")
        print(f"Name : {self.__name}")
        print(f"Age : {self.__age}")
        print(f"Contact : {self.__contact}")
        print(f"Balance : {self.__amount}")
        print("____________________________________________________________________")
    
    def deposite(self):
        deposite_amount = float(input("Enter here the amount you want to deposite : "))
        self.__amount +=deposite_amount
        print(f"The amount is deposited successfully\nNow the balance is : {self.__amount}\n")
    
    def withdraw(self):
        withdraw_amount = float(input("Enter here the amount you want to withdraw : "))
        if withdraw_amount<self.__amount:
            self.__amount -=withdraw_amount
            print(f"The amount is deducted from the bank \nNow the balance left is : {self.__amount}\n")


        else:
            print("You don't have the enough balance in your account ")

s1 = SavingsAccount("kashish",20,7489619180,100000)
c1 = CurrentAccount("Piysh", 23,7945420934,100000)

s1.details()
print()
c1.details()
print()

s1.deposite()
c1.withdraw()

