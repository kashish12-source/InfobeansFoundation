# 29. Employee Attendance

# Abstract:

# Employee

# Derived:

# FullTimeEmployee
# PartTimeEmployee

# Calculate working hours.

collection = []
def add_to_collection(obj):
    collection.append(obj)

from abc import ABC ,abstractmethod

class Employee(ABC):
    @abstractmethod
    def employee_details(self):
        pass 

    @abstractmethod
    def calculate_salary(self):
        pass
    
    @abstractmethod
    def validate_employee(self):
        pass 

    @abstractmethod
    def calculate_increment(self):
        pass


class RegisterEmployee:
    def __init__(self,id ,name ,contact, salary , worked_days):
        self.__id = id 
        self.__name = name 
        self.__contact = contact
        self.__salary =salary
        self.__worked_days = worked_days
    
    def get_id(self):
        return self.__id

    def get_details(self):
        return self.__id ,self.__name,self.__contact,self.__salary,self.__worked_days,

class FullTimeEmployee(Employee):
    def __init__(self,id):
        self.__id = id 
        self.__valid_employee =False
        self.__obj = None 

    def validate_employee(self):
        for obj in collection:
            if obj.get_id() == self.__id:
                self.__obj = obj
                self.__valid_employee = True
                print("Employee is registerd ")
                return True
        print("Sorry Employee is not registered")
        return False

    def employee_details(self):
        if self.__valid_employee:
            id ,name,contact,salary,worked_days = self.__obj.get_details()

            print("=======Details of an Employee =======")
            print(f"ID : {id}\nNAE: {name} \nCONTACT : {contact}\nSALARY  / DAY: {salary} \nWORKED DAYS : {worked_days} ")
            print("\n=================================\n")
        
    def calculate_salary(self):
        if self.__valid_employee:
            id ,name,contact,salary,worked_days= self.__obj.get_details()
            print(f"Salary of an employee is : {salary*worked_days} rupees ")
    
    def calculate_increment(self):
        if self.__valid_employee:
            id ,name,contact,salary,worked_days= self.__obj.get_details()
            if worked_days >=25 and worked_days<=30:
                print(f"Employee get an increment of : {15000} rupees")

            elif worked_days >=20 and worked_days<25:
                print(f"Employee get an increment of : {1000} rupees")
            else:
                print("Employee made a lots of holidays so they didn't get any increment")


class PartTimeEmployee(Employee):
    def __init__(self,id):
        self.__id = id 
        self.__valid_employee =False
        self.__obj = None 

    def validate_employee(self):
        for obj in collection:
            if obj.get_id() == self.__id:
                self.__obj = obj
                self.__valid_employee = True
                print("Employee is registerd ")
                return True
        print("Sorry Employee is not registered")
        return False

    def employee_details(self):
        if self.__valid_employee:
            id ,name,contact,salary,worked_days = self.__obj.get_details()

            print("=======Details of an Employee =======")
            print(f"ID : {id}\nNAE: {name} \nCONTACT : {contact}\nSALARY  / DAY: {salary} \nWORKED DAYS : {worked_days} ")
            print("\n=================================\n")
        
    def calculate_salary(self):
        if self.__valid_employee:
            id ,name,contact,salary,worked_days = self.__obj.get_details()
            print(f"Salary of an employee is : {salary*worked_days} rupees ")
    
    def calculate_increment(self):
        if self.__valid_employee:
           print("The Part Time employee didn't get any increment as they are already comming only for the half of the time compare to the Full Time Employee")

e1 = RegisterEmployee(101,"kashish",7489619180,2000,24)
e2 = RegisterEmployee(102,"koshiki",9009760717, 2400,20)

add_to_collection(e1)
add_to_collection(e2)

f1 = FullTimeEmployee(101)
f2 =PartTimeEmployee(102)

f1.validate_employee()
f1.employee_details()
f1.calculate_salary()
f1.calculate_increment()

f2.validate_employee()
f2.employee_details()
f2.calculate_salary()
f2.calculate_increment()
