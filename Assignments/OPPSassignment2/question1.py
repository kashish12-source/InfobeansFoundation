# 1. Employee Management System
# Problem

# Create an Employee class to manage employee details.

# Requirements

# Each employee should have:

# employee id
# name
# department
# salary
# Functionalities
# Display employee details
# Increase salary by percentage
# Count total employees created using a class variable

# Create employee object from a string:

# "101-Rahul-IT-50000"

# using a class method.

# Concepts Practiced
# constructor
# instance variables
# class variables
# class method
# instance methods


class Employee:
    company_name ="GOOGLE"#this is the static variable
    counter = 0
    def __init__(self,content):
        id , name ,department,salary =content.split("-")
        Employee.counter+=1
        self.__id = id
        self.__name = name
        self.__department = department
        self.__salary = salary

    def display_details(self):
        print(f"___________________________{Employee.company_name}____________________________")
        print(f"\nID -> {self.__id}\nNAME -> {self.__name.upper()}\nDEPARTMENT -> {self.__department.upper()}\nSALARY -> {self.__salary}")
        print()
        print(f"______________________________________________________________________________")

    def increase_salary(self):
        per = float(input("Enter the percentage here : "))
        salary = float(self.__salary)
        increment = (salary*(per/100))
        salary +=increment
        self.__salary = salary
        print(f"After increment salary is : {self.__salary}")
        
        return self.__salary
    @classmethod
    def count_employees (cls):
        print(f"The no. of employees in {Employee.company_name} is : {Employee.counter}")

e1 = Employee("101-Rahul-IT-50000")
e1.display_details()
e2 = Employee("102-Rahul-IT-50000")
e2.display_details()
e2.increase_salary()
Employee.count_employees()
