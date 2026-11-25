# # 22. Payment Gateway

# # Abstract class Payment.

# # Derived:

# # CreditCard
# # UPI
# # Wallet

# # Implement payment processing.

from abc import ABC , abstractmethod

collection =[]

def display_users():
    for obj in collection:
        print(obj.get_name(),obj.get_balance())



class Payment(ABC):
    @abstractmethod
    def check_user(self):
        pass 


    @abstractmethod
    def validate_amount(self):
        pass

    @abstractmethod
    def make_payment(self):
        pass

    @abstractmethod
    def deposit_amount(self):
        pass 


class User:
    def __init__(self,id,name,pin,balance):
        self.__id = id
        self.__name = name 
        self.__pin = pin
        self.__balance = balance

    def get_id(self):
        return self.__id

    def get_pin (self):
        return self.__pin
    
    def get_name(self):
        return self.__name

    def deduct_amount(self,amount):
        self.__balance -=amount
        return self.__balance

    def add_amount(self,amount):
        self.__balance += amount
        return self.__balance

    def get_balance (self):
        return self.__balance

    def add_user(self):

        for obj in collection:
            if obj.get_id() == self.get_id():
                print("User already exists")
                return

        collection.append(self)
        print("User added successfully")


class CreditCard(Payment):
    def __init__(self, id ,pin , amount):
        self.__id = id 
        self.__pin = pin
        self.__amount = amount 
    
    __validate = False
    def check_user(self,obj):
        for obj in collection:
            if obj.get_id() ==self.__id:
                if self.__pin ==obj.get_pin():
                    CreditCard.__validate = True
                    print("User is validated successfully")
                    return
        
        print("User is not validated")
    __enough_amount = False
    def validate_amount(self,amount,obj):
        if obj in collection :
            if obj.get_balance() >= amount:
                print("You have enough balance ")
                CreditCard.__enough_amount =True

            else:
                print("You don't have enough balance ")
        else:
            print("The user is not found ")


    def make_payment(self,amount,obj):
        if CreditCard.__enough_amount and CreditCard.__validate :
            bal = obj.deduct_amount(amount)
            print(f"Now the balance left is : {bal}")
        elif not CreditCard.__enough_amount:
            print("you don't have enough amount ")
        else:
            print("Your credentials are not valid ")
    
    def deposit_amount(self,amount,obj):
        if CreditCard.__validate:
            bal = obj.add_amount(amount)
            print(f"Your amount is deposited now the balance is : {bal}")
        else:
            print("Payment cannot be proceeded")
    


class UPI(Payment):
    def __init__(self,id,pin,amount):
        self.__id = id 
        self.__pin = pin
        self.__amount = amount 

    __valid_user = False
    def check_user(self,obj):
        if obj.get_id ()== self.__id and obj.get_pin() == self.__pin:
            print("Your credentials are valid")
            
            UPI.__valid_user= True
            return
        print("Your credentials are not valid")

    __is_able =False
    def validate_amount(self,obj):
        if UPI.__valid_user :
            if obj.get_balance() >= self.__amount:
                print("You have enough balance in your account to made transactions ")
                UPI.__is_able=True
                return 
            else:
                print("You don't have enough balance to make transactions")
        else:
            print("Your credentials are not correct so you are not able to made any transaction")
    
    def make_payment(self,obj):
        if UPI.__is_able :
            bal = obj.deduct_amount(self.__amount)
            print(f"Now the payment left in your account is : {bal}")
            
        else:
            print(f"Payment cannot be proceeded ")
    
    def deposit_amount(self,obj):
        if UPI.__is_able and self.__amount>0:
            bal = obj.add_amount(self.__amount)
            print(f"Now your balance is : {bal}")
        else:
            print("Your payment is no proceeded")
    

class Wallet(Payment):
    def __init__(self,id,pin,amount):
        self.__id = id 
        self.__pin = pin
        self.__amount = amount 
    
    __validate_user = False
    def check_user(self,obj):
        if obj.get_id() == self.__id and obj.get_pin() == self.__pin:
            Wallet.__validate_user = True
            print("Your credentials are valid")
        else:
            print("Enter the valid credentials ")

    __enough_amount = False
    def validate_amount(self,obj):
        if obj.get_balance() >= self.__amount:
            Wallet.__enough_amount= True
            print("You have enough balance in your account ")
            return Wallet.__enough_amount
        else:
            print("You don't have enough balance in your account ")
            return Wallet.__enough_amount

    def make_payment(self,obj):
        if Wallet.__enough_amount and Wallet.__validate_user:
            bal = obj.deduct_amount(self.__amount)
            print(f"Now the balance left in your account is : {bal}")
        else:
            print("Payment not proceeded")
    
    def deposit_amount(self,obj):
        if Wallet.__enough_amount and Wallet.__validate_user:
            bal = obj.add_amount(self.__amount)
            print(f"Now the balance is : {bal}")
        else:
            print("Payment not proceeded")


u1 = User(101,"Kahsish",123,200000)
u2 = User(101,"Kahsish",123,200000)
u1.add_user()
print("\n========== CREDIT CARD ==========")

c = CreditCard(101, 123, 2000)

c.check_user(u1)
c.validate_amount(2000, u1)
c.make_payment(2000, u1)
c.deposit_amount(40000, u1)

display_users()
print("\n========== UPI ==========")

upi = UPI(102, 456, 3000)

upi.check_user(u2)
upi.validate_amount(u2)
upi.make_payment(u2)
upi.deposit_amount(u2)

display_users()
print("\n========== WALLET ==========")

wallet = Wallet(101, 123, 5000)

wallet.check_user(u1)
wallet.validate_amount(u1)
wallet.make_payment(u1)
wallet.deposit_amount(u1)

display_users()