# 3. Employee Management

# Base class Employee.

# Derived:

# Developer
# Tester
# HR

# Calculate salaries differently.

from abc import ABC , abstractmethod

class Employee(ABC):
    
    @abstractmethod
    def details(self):
        pass 

    @abstractmethod
    def bonous(self):
        pass 

class Developer(Employee):
    def __init__(self, name ,age ,contact,salary,days):
        self.__name = name 
        self.__age = age 
        self.__contact = contact 
        self.__salary = salary
        self.__days = days

    def details(self):
        print("The details of an Employee is here : ")
        print(f"Name : {self.__name}")
        print(f"Age : {self.__age}")
        print(f"Contact : {self.__contact}")
        print(f"Salary : {self.__salary}\n")


    def bonous(self):
        if self.__days >25:
            self.__salary+=self.__salary/10
            print(f"You get bonous of 10 % \nNow you final salary is : {self.__salary}\n")
        elif 20<self.__days<25:
            self.__salary += self.__salary*0.05

            print(f"You get bonous of 5%\nNow your final salary is : {self.__salary}\n")

        else:
            print("You don't get any bonous because you took too much of leave \n")


class Tester(Employee):
    def __init__(self , name , id ,contact,experiance):
        self.__name = name 
        self.__id = id 
        self.__contact = contact 
        self.__experiance = experiance
    
    def details(self):
        print("The details of an Tester is here : ")
        print(f"Name : {self.__name}")
        print(f"ID : {self.__id}")
        print(f"Contact : {self.__contact}")
        print(f"Experiance : {self.__experiance}")
        print()
    
    def bonous(self):
        if self.__experiance>10:
            print("you get 10000 as a bonous in your salary\n")
        elif 8< self.__experiance <10:
            print("you get 8000 as a bonous in your salary\n")
        elif 5<self.__experiance <=8:
            print("you get 5000 as a bonous in your salary\n")
        else:
            print("You don't get any bonous at all work hard and be the consitent part of the organisation to get the bonous next time \n")
        
class HR(Employee):
    def __init__(self, name ,age ,department, salary,days):
        self.__name = name 
        self.__age = age 
        self.__department = department
        self.__salary = salary
        self.__days = days


    def details(self):
        print("The details of an Tester is here : ")
        print(f"Name : {self.__name}")
        print(f"Age : {self.__age}")
        print(f"Department : {self.__department}")
        print(f"Salary : {self.__salary}")
        print()


    def bonous(self):
        if self.__days>25:
            print("Bonus amount is : 10000\n")
        elif 20<self.__days<=25:
            print("Bonous amount is : 7000\n")
        else:
            print("You don't get any bonous at all work hard and be the consitent part of the organisation to get the bonous next time \n")

hr = HR("Kashish", 20,"CSE", 50000,26)
tes = Tester("keshav",101,7489619180,23)
dev = Developer("Piyush ", 23,75348962,300000,24)

hr.details()
hr.bonous()
print("\n\n")
tes.details()
tes.bonous()
print("\n\n")
dev.details()
dev.bonous()

