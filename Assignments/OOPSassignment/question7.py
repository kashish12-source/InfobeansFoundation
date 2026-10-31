# 7. Write a Java program to create a class called "Bank" with a collection of accounts and methods to add and remove accounts, and to deposit and withdraw money. Also define a class called "Account" to maintain account details of a particular customer.
class Bank:
    def __init__(self):
        self.collection={}
    def add_account(self,details,account_no):
        self.collection[account_no] = details
        print("account is added successfully ")

    

    
    def remove_account(self,account_no):
        if account_no in self.collection.keys():
            del self.collection[account_no]
            print("account is deleted successfully ")
        else:
            print("account no. not found ")


        # for i in Bank.collection.keys():
        #     if n == i:
        #         del i
        #         print("account deletion is successfull")
        #     else:
        #         print("Account not found ")
            
    def deposit_amount(self,account_no, amount):
        if account_no in self.collection.keys():
            self.collection[account_no].deposit(amount)
        else:
            print("Account not found")


        


    def withdraw_amount(self,account_no, amount):
        if account_no in self.collection.keys():
            self.collection[account_no].withdraw(amount)

        else:
            print("Account not found ")
        # a = float(input("Enter a withdraw amount here : "))
        # if a > self.__balance:
        #     print("The balance is not enough")
        # else:
        #     self.__balance -=a
            # print(f"After withdraw the amount left is : {self.__balance}")

class Account:
    def __init__ (self,name,contact,email,address,balance):
        self.__name = name
        self.__contact = contact
        self.__email = email
        self.__address  = address 
        self.__balance = balance 
    
    def account_details(self):
        print("_____________________________ACCOUNT DETAILS______________________________")
        print(f"Name : {self.__name}")
        print(f"Contact : {self.__contact}")
        print(f"Email : {self.__email}")
        print(f"Address : {self.__address}")
        print(f"Balance: {self.__balance}")
        print("__________________________________________________________________________")


    def check_balance(self):
        print(f"Your current balance is : {self.__balance}")
    
    def deposit(self,amount):
        if amount > 0:
            self.__balance +=amount
            print(f"Diposited :{amount}" )
            print(f"Updated balance is :{self.__balance}")

        else:
            print("account not found to deposite")
        

    def withdraw(self,amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Money withdrawn: {amount}")
            print(f"Remaining balance: {self.__balance}")
        else:
            print("Insufficient balance or invalid amount")


a1 = Account("kashish","34589742057","kashish@gmail.com","388-c prajapat nagar",4000000)
b1 = Bank()
a1.check_balance()
a1.account_details()
b1.add_account(a1,101)
b1.deposit_amount(101,459)
