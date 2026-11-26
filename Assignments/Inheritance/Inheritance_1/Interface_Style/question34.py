# 34. Cloud Storage Interface

# Methods:

# upload()
# download()

# Implement:

# GoogleDrive
# Dropbox

collection = []
def add_to_collection(obj):
    collection.append(obj)

from abc import ABC,abstractmethod
class Storage(ABC):
    @abstractmethod
    def check_account(self):
        pass 

    @abstractmethod
    def upload(self):
        pass

    @abstractmethod
    def download(self):
        pass 

class RegisterUser:
    def __init__(self,name,id):
        self.__name = name 
        self.__id = id 


    def get_name (self):
        return self.__name 

    def get_id (self):
        return self.__id

    
class GoogleDrive(Storage):
    def __init__(self,id):
        self.__id = id 
        self.__validate = False
        self.__obj = None
    
    def check_account(self):
        for obj in collection :
            if obj.get_id() == self.__id:
                self.__validate = True
                self.__obj = obj
                print("Account is valid")

                return True
        
        print("Account is not valid")
        return False

    def upload(self):
        if self.__validate:
            print("Media is uploaded successfully on the drive ")
        
    def download(self):
        if self.__validate:
            print("Media is downloaded on the drive ")
    
    
class DropBox(Storage):
    def __init__(self,id):
        self.__id = id 
        self.__validate = False
        self.__obj = None
    
    def check_account(self):
        for obj in collection :
            if obj.get_id() == self.__id:
                self.__validate = True
                self.__obj = obj
                print("Account is valid")

                return True
        
        print("Account is not valid")
        return False

    def upload(self):
        if self.__validate:
            print("Media is uploaded successfully on the dropBox ")

        
    def download(self):
        if self.__validate:
            print("Media is downloaded on the dropBox ")

    
a1 = RegisterUser("kashish",101)
a2 = RegisterUser("koshiki",102)

add_to_collection(a1)
add_to_collection(a2)

d1 = DropBox(101)
g1 = GoogleDrive(102)
print("\n==============Drive check===============")
d1.check_account()
d1.upload()
d1.download()

print("\n=============DropBox check==============")
g1.check_account()
g1.upload()
g1.download()



