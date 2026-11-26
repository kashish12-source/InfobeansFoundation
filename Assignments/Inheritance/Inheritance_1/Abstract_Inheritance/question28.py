# 28. Authentication System

# Abstract:

# Authentication

# Derived:

# OTPAuth
# GoogleAuth
# FacebookAuth


from abc import ABC ,abstractmethod

collection = []
def add_to_collection (obj):
    collection.append(obj)
    print("object added successfully")

class Authentication(ABC):

    @abstractmethod
    def display_details(self):
        pass 
    
    @abstractmethod
    def validate_credential(self):
        pass

class RegisterUser:
    def __init__(self, name ,email, password,id ):
        self.__name = name 
        self.__email = email
        self.__password = password 
        self.__id = id 
        self.__valid_user =False
        self.__obj = None
    
    def get_details(self):
        return self.__name ,self.__email
    
    def get_password(self):
        return self.__password
    
    def get_id (self):
        return self.__id

class OTPAuth(Authentication):
    def __init__(self, name ,id ,email,password):
        self.__name = name 
        self.__id = id 
        self.__email = email
        self.__password=password
        self.__validate_user = False 
        self.__obj = None 

    def validate_credential(self):
        for obj in collection:
            if obj.get_id() == self.__id :
                
                if obj.get_password() == self.__password:
                    print("Your credentials are valid ")
                    self.__obj = obj
                    self.__validate_user =True
                    return True
                else:
                    print("Your password is not valid")
                    return False

        print("User not registered ")
        return False
    
    def display_details(self):
        if self.__validate_user:
            name,email = self.__obj.get_details()

            print(f"Name: {name}")
            print(f"Email : {email}")
            print(f"Id : {self.__obj.get_id()}")
    
    
        
class FacebookAuth(Authentication):

    def __init__(self, name ,id ,email,password):
        self.__name = name 
        self.__id = id 
        self.__email = email
        self.__password=password
        self.__validate_user = False 
        self.__obj = None 

    def validate_credential(self):
        for obj in collection:
            if obj.get_id() == self.__id :
                
                if obj.get_password() == self.__password:
                    print("Your credentials are valid ")
                    self.__obj = obj
                    self.__validate_user =True
                    return True
                else:
                    print("Your password is not valid")
                    return False
            
        print("User not registered ")
        return False
    
    def display_details(self):
        if self.__validate_user:
            name,email = self.__obj.get_details()

            print(f"Name: {name}")
            print(f"Email : {email}")
            print(f"Id : {self.__obj.get_id()}")
    
    
        




class GoogleAuth(Authentication):
    def __init__(self, name ,id ,email,password):
        self.__name = name 
        self.__id = id 
        self.__email = email
        self.__password=password
        self.__validate_user = False 
        self.__obj = None 

    def validate_credential(self):
        for obj in collection:
            if obj.get_id() == self.__id :
                
                if obj.get_password() == self.__password:
                    print("Your credentials are valid ")
                    self.__obj = obj
                    self.__validate_user =True

                    return True
                else:
                    print("Your password is not valid")
                    return False
            
        print("User not registered ")
        return False
    
    def display_details(self):
        if self.__validate_user:
            name,email = self.__obj.get_details()

            print(f"Name: {name}")
            print(f"Email : {email}")
            print(f"Id : {self.__obj.get_id()}")
    
    
u1 = RegisterUser("kashish","kashishvishnoi2006@gmail.com",123,101)
u2 = RegisterUser("koshiki","koshiki@gmail.com",1234,102)
u3 = RegisterUser("piyush","piyush@gmail.com",234,103)

add_to_collection(u1)
add_to_collection(u2)
add_to_collection(u3)

o1 = OTPAuth("Kashish",101,"kashishvishnoi2006@gmail.com",123)

g1 = GoogleAuth("koshiki",102,"koshiki@gmail.com",1234)

f1 = FacebookAuth("piyush",103,"piyush@gmail.com",234)

print("\n===========================Check otp authentication========================\n")

o1.validate_credential()
o1.display_details()


print("\n===========================Check Google authentication========================\n")
g1.validate_credential()
g1.display_details()

print("\n===========================Check otp authentication========================\n")
f1.validate_credential()
f1.display_details()











