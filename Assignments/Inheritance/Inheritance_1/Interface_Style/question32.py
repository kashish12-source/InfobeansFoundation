# 32. Database Interface

# Methods:

# connect()
# disconnect()

# Implement:

# MySQL
# MongoDB
# PostgreSQL

collection = []
def add_to_collection(obj):
    collection.append(obj)


from abc import ABC , abstractmethod

class Database(ABC):

    @abstractmethod
    def connect(self):
        pass 

    @abstractmethod
    def disconnect(self):
        pass 

    @abstractmethod
    def validate_account(self):
        pass 
class CreateAccont:
    def __init__(self, id, name ,password):
        self.__id =id 
        self.__name = name 
        self.__password = password
    
    def get_id (self):
        return self.__id
    
    def get_name (self):
        return self.__name 

    def get_password(self):
        return self.__password


class MySql(Database):
    def __init__(self,name,id,password):
        self.__name = name 
        self.__id = id 
        self.__password = password
        self.__valid_id =False
        self.__obj = None
    
    def validate_account(self):
        for obj in collection:
            if obj.get_id() == self.__id and obj.get_password() == self.__password:
                
                    self.__valid_id = True
                    self.__obj = obj
                    print("The account is valid ")

                    return True

        print("Account is not valid ")
        return False
    def connect(self):
        if self.__valid_id:
            print("Connection is established by: ")
            print(f"{self.__obj.get_name()} with the id : {self.__obj.get_id()} and the passwords :{self.__obj.get_password()}")

        
    def disconnect(self):
        if self.__valid_id:
            print("Connection is established by: ")
            print(f"{self.__obj.get_name()} with the id : {self.__obj.get_id()} and the passwords :{self.__obj.get_password()}")
            


class MongoDB(Database):
    def __init__(self,name,id,password):
        self.__name = name 
        self.__id = id 
        self.__password = password
        self.__valid_id =False
        self.__obj = None
    
    def validate_account(self):
        for obj in collection:
            if obj.get_id() == self.__id and obj.get_password() == self.__password:
                
                    self.__valid_id = True
                    self.__obj = obj
                    print("The account is valid ")

                    return True

        print("Account is not valid ")
        return False
    def connect(self):
        if self.__valid_id:
            print("Connection is established by: ")
            print(f"{self.__obj.get_name()} with the id : {self.__obj.get_id()} and the passwords :{self.__obj.get_password()}")

        
    def disconnect(self):
        if self.__valid_id:
            print("Connection is established by: ")
            print(f"{self.__obj.get_name()} with the id : {self.__obj.get_id()} and the passwords :{self.__obj.get_password()}")
            

class PostgreSql(Database):
    def __init__(self,name,id,password):
        self.__name = name 
        self.__id = id 
        self.__password = password
        self.__valid_id =False
        self.__obj = None
    
    def validate_account(self):
        for obj in collection:
            if obj.get_id() == self.__id and obj.get_password() == self.__password:
                
                    self.__valid_id = True
                    self.__obj = obj
                    print("The account is valid ")

                    return True

        print("Account is not valid ")
        return False
    def connect(self):
        if self.__valid_id:
            print("Connection is established by: ")
            print(f"{self.__obj.get_name()} with the id : {self.__obj.get_id()} and the passwords :{self.__obj.get_password()}")

        
    def disconnect(self):
        if self.__valid_id:
            print("Connection is established by: ")
            print(f"{self.__obj.get_name()} with the id : {self.__obj.get_id()} and the passwords :{self.__obj.get_password()}")


# Creating account objects

a1 = CreateAccont(101, "Kashish", "12345")
a2 = CreateAccont(102, "Rahul", "abc123")
a3 = CreateAccont(103, "Priya", "pass123")

# Adding accounts to collection

add_to_collection(a1)
add_to_collection(a2)
add_to_collection(a3)


# Creating database objects

mysql = MySql("Kashish", 101, "12345")

mongodb = MongoDB("Rahul", 102, "abc123")

postgresql = PostgreSql("Priya", 103, "pass123")


print("\n--- MySQL ---")
mysql.validate_account()
mysql.connect()
mysql.disconnect()


print("\n--- MongoDB ---")
mongodb.validate_account()
mongodb.connect()
mongodb.disconnect()

print("\n--- PostgreSQL ---")
postgresql.validate_account()
postgresql.connect()
postgresql.disconnect()
