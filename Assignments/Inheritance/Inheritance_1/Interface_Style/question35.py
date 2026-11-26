# 35. Messaging Application

# Methods:

# send_message()

# Implement:

# WhatsApp
# Telegram
# Signal
collection = []
def add_to_collection(obj):
    collection.append(obj)

from abc import ABC ,abstractmethod
class Messaging(ABC):

    @abstractmethod
    def sendmessage(self):
        pass 

    @abstractmethod
    def check_reciver(self):
        pass 

    @abstractmethod
    def validate_account(self):
        pass 

class RegisterUser:
    def __init__(self,id ,name ,contact,email):
        self.__id = id 
        self.__name = name 
        self.__contact = contact 
        self.__email =email

    def get_id(self):
        return self.__id
    
    def get_detail(self):
        return self.__name ,self.__contact,self.__email
    

class Whatsapp(Messaging):
    def __init__(self,id,reciver_id):
        self.__id = id 
        self.__r_id = reciver_id
        self.__validate_account = False
        self.__validate_account_r= False
        self.__obj = None
    
    def validate_account(self):
        for obj in collection:
            if obj.get_id() == self.__id:
                print("Account is valid")
                self.__validate_account = True
                self.__obj = obj 
                return True

        print("Account is not valid ")
        return False

    def check_reciver(self):
        for obj in collection:
            if obj.get_id() == self.__r_id:
                print("reciver is valid ")
                self.__validate_account_r = True
                return True
        return False

    def sendmessage(self):
        if self.__validate_account_r and self.__validate_account:
            print("Message sent")
        else:
            print("Message can't be sent")

class Telegram(Messaging):
    def __init__(self,id,reciver_id):
        self.__id = id 
        self.__r_id = reciver_id
        self.__validate_account = False
        self.__validate_account_r= False
        self.__obj = None
    
    def validate_account(self):
        for obj in collection:
            if obj.get_id() == self.__id:
                print("Account is valid")
                self.__validate_account = True
                self.__obj = obj 
                return True

        print("Account is not valid ")
        return False

    def check_reciver(self):
        for obj in collection:
            if obj.get_id() == self.__r_id:
                print("reciver is valid ")
                self.__validate_account_r = True
                return True
        return False

    def sendmessage(self):
        if self.__validate_account_r and self.__validate_account:
            print("Message sent")
        else:
            print("Message can't be sent")


class Signal(Messaging):
    def __init__(self,id,reciver_id):
        self.__id = id 
        self.__r_id = reciver_id
        self.__validate_account = False
        self.__validate_account_r= False
        self.__obj = None
    
    def validate_account(self):
        for obj in collection:
            if obj.get_id() == self.__id:
                print("Account is valid")
                self.__validate_account = True
                self.__obj = obj 
                return True

        print("Account is not valid ")
        return False

    def check_reciver(self):
        for obj in collection:
            if obj.get_id() == self.__r_id:
                print("reciver is valid ")
                self.__validate_account_r = True
                return True
        return False

    def sendmessage(self):
        if self.__validate_account_r and self.__validate_account:
            print("Signal matched")
        else:
            print("Signal can't be sent")


# Creating users

u1 = RegisterUser(101, "Kashish", "9876543210", "kashish@gmail.com")
u2 = RegisterUser(102, "Rahul", "9876543211", "rahul@gmail.com")
u3 = RegisterUser(103, "Priya", "9876543212", "priya@gmail.com")

# Adding users to collection

add_to_collection(u1)
add_to_collection(u2)
add_to_collection(u3)


# Creating messaging objects

w1 = Whatsapp(101, 102)
t1 = Telegram(102, 103)
s1 = Signal(103, 101)


# Testing WhatsApp

print("\n--- WhatsApp ---")
w1.validate_account()
w1.check_reciver()
w1.sendmessage()


# Testing Telegram

print("\n--- Telegram ---")
t1.validate_account()
t1.check_reciver()
t1.sendmessage()


# Testing Signal

print("\n--- Signal ---")
s1.validate_account()
s1.check_reciver()
s1.sendmessage()
