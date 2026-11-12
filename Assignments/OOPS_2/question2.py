# 2. Bank Account Simulation
# Problem

# Design a banking system using OOP.

# Requirements

# Each account should contain:

# account number
# holder name
# balance
# Functionalities
# Deposit money
# Withdraw money
# Prevent withdrawal if balance insufficient
# Display account summary
# Maintain bank-wide interest rate as class variable
# Add static method to validate minimum balance rule
# Concepts Practiced
# object state management
# static methods
# class variables
# validations

class Bank:
    interest_rate = 5
    bank_name = "SBI"
    def __init__(self,account_number , name , balance):
        self.__account_number = account_number
        self.__name = name 
        self.__balance = balance
    
    def deposit(self):
        amount = float(input("Enter the amount you want to deposite : "))
        self.__balance = float(self.__balance)+amount
        print(f"The balance after depositing money is : {self.__balance}")

    @staticmethod
    def preventions(balance):
        if balance>2000:
            return True
        return False

    def withdraw(self):
        amount = float(input("Enter the amount you want to withdraw: "))

        if amount > 0 and amount <= self.__balance:
            if Bank.preventions(self.__balance - amount):
                self.__balance -= amount
                print("Money withdrawal is successful")
                print(f"Remaining balance: {self.__balance}")
            else:
                print("Minimum balance rule violated")
        else:
            print("Insufficient balance or invalid amount")
    
    def display_details(self):
        print(f"___________________________{Bank.bank_name}________________________")
        print(f"\nNAME : {self.__name.upper()}\nACCOUNT NUMBER : {self.__account_number}\nBALANCE : {self.__balance}\nINTEREST RATE :{Bank.interest_rate}")
        print("\n____________________________________________________________________")

b1 = Bank(101,"kashish",32098)
b1.display_details()
b1.withdraw()
b1.deposit()
b1.display_details()
