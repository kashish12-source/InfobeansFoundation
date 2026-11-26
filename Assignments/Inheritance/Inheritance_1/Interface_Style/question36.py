# 36. Payment Interface

# Methods:

# pay()

# Implement:

# PayPal
# Stripe
# Razorpay

collection = []
def add_to_collection(obj):
    collection.append(obj)


from abc import ABC ,abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass 

    @abstractmethod
    def validate_user(self):
        pass 

    @abstractmethod
    def validate_reciver(self):
        pass 

class RegisterUser:
    def __init__(self,account_no,name):
        self.__account_no = account_no
        self.__name = name 

    def get_account(self):
        return self.__account_no
    
    def get_name (self):
        return self.__name

class PayPal(Payment):
    def __init__(self,account_no,reciver_account):
        self.__account_no = account_no
        self.__reciver_acc = reciver_account
        self.__validate = False
        self.__obj = None 
        self.__validate_r = False

    def validate_user(self):
        for obj in collection :
            if obj.get_account()== self.__account_no:
                self.__validate = True
                self.__obj = obj 
                print("Account details are valid ")
                return True
            
        print("Account details are not valid ")
        return False 

    def validate_reciver(self):
        for obj in collection:
            if obj.get_account() == self.__reciver_acc:
                self.__validate_r = True
                print("Reciverd details are valid ")
                return True
        print("Recivers details are invalid ")
        return False
    
    def pay(self):
        if self.__validate_r and self.__validate:
            amount = int(input("Enter the amount here : "))
            print(f"{amount} is paid now")



class RazorPay(Payment):
    def __init__(self,account_no,reciver_account):
        self.__account_no = account_no
        self.__reciver_acc = reciver_account
        self.__validate = False
        self.__obj = None 
        self.__validate_r = False

    def validate_user(self):
        for obj in collection :
            if obj.get_account() == self.__account_no:
                self.__validate = True
                self.__obj = obj 
                print("Account details are valid ")
                return True
            
        print("Account details are not valid ")
        return False 

    def validate_reciver(self):
        for obj in collection:
            if obj.get_account() == self.__reciver_acc:
                self.__validate_r = True
                print("Reciverd details are valid ")
                return True
        print("Recivers details are invalid ")
        return False
    
    def pay(self):
        if self.__validate_r and self.__validate:
            amount = int(input("Enter the amount here : "))
            print(f"{amount} is paid now")



class Stripe(Payment):
    def __init__(self,account_no,reciver_account):
        self.__account_no = account_no
        self.__reciver_acc = reciver_account
        self.__validate = False
        self.__obj = None 
        self.__validate_r = False

    def validate_user(self):
        for obj in collection :
            if obj.get_account() == self.__account_no:
                self.__validate = True
                self.__obj = obj 
                print("Account details are valid ")
                return True
            
        print("Account details are not valid ")
        return False 

    def validate_reciver(self):
        for obj in collection:
            if obj.get_account() == self.__reciver_acc:
                self.__validate_r = True
                print("Reciverd details are valid ")
                return True
        print("Recivers details are invalid ")
        return False
    
    def pay(self):
        if self.__validate_r and self.__validate:
            amount = int(input("Enter the amount here : "))
            print(f"{amount} is paid now")
            print(f"You get a cashback of : ")
            if amount>=20000:
                print(1000)
            elif amount<10000:
                print(200)
            


# Creating users

u1 = RegisterUser(101, "Kashish")
u2 = RegisterUser(102, "Rahul")
u3 = RegisterUser(103, "Priya")

# Adding users to collection

add_to_collection(u1)
add_to_collection(u2)
add_to_collection(u3)


# Creating payment objects

p1 = PayPal(101, 102)
p2 = RazorPay(102, 103)
p3 = Stripe(103, 101)


# Testing PayPal

print("\n--- PayPal ---")
p1.validate_user()
p1.validate_reciver()
p1.pay()


# Testing RazorPay

print("\n--- RazorPay ---")
p2.validate_user()
p2.validate_reciver()
p2.pay()


# Testing Stripe

print("\n--- Stripe ---")
p3.validate_user()
p3.validate_reciver()
p3.pay()

