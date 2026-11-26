# 37. Social Login System

# Methods:

# login()

# Implement:

# GoogleLogin
# GitHubLogin
# LinkedInLogin
collection ={}
from abc import ABC, abstractmethod
class Login(ABC):
    
    @abstractmethod
    def validate_credential(self):
        pass 

    @abstractmethod
    def login(self):
        pass 

class GoogleLogin(Login):
    def __init__(self,name,id,email):
        self.__name = name 
        self.__id = id 
        self.__email = email

    def login(self):
        collection[self.__id] = {"name":self.__name,"email": self.__email}
        print("Login successfully")
    
    def validate_credential(self):
        if self.__id in collection.keys():

            print("Valid credentials")
        else:
            print("credentials are not valid ")
class GithubLogin(Login):
    def __init__(self,name,user_id,email):
        self.__name = name 
        self.__user_id = user_id 
        self.__email = email

    def login(self):
        collection[self.__user_id] = {"name":self.__name,"email": self.__email}
        print("Login successfully")
    
    def validate_credential(self):
        if self.__user_id in collection.keys():

            print("Valid credentials")
        else:
            print("credentials are not valid ")
class LinkedinLogin(Login):
    def __init__(self,name,id,email):
        self.__name = name 
        self.__id = id 
        self.__email = email

    def login(self):
        collection[self.__id] = {"name":self.__name,"email": self.__email}
        print("Login successfully")
    
    def validate_credential(self):
        if id in collection.keys():

            print("Valid credentials")
        else:
            print("credentials are not valid ")

obj1 = GoogleLogin("Kashish", 101, "kashish@gmail.com")

obj2 = GithubLogin("Rahul", 102, "rahul@gmail.com")

obj3 = LinkedinLogin("Priya", 103, "priya@gmail.com")
obj1.login()
obj2.login()
obj3.login()

obj1.validate_credential()
obj2.validate_credential()
obj3.validate_credential()

print(collection)