
# 1. Employee Bonus Calculator
# Problem Statement

# A company gives bonuses differently based on employee type.

# Create:

# abstract class Employee
# child classes:
# Developer
# Manager
# Intern

# Rules:

# Developer → 20% bonus
# Manager → 35% bonus
# Intern → fixed ₹5000 bonus
# Requirements

# Methods:

# calculate_bonus()
# display_details()
# Concepts
# Abstract class
# Method overriding
# Business logic


from abc import ABC , abstractmethod

class Employee(ABC):
    def __init__(self, name ,id,salary):
        self.__name = name 
        self.__id = id 
        
        self.__salary = salary
    
    @abstractmethod
    def calculate_bonous(self):
        pass 

    def get_salary(self):
        return self.__salary

    def __str__(self):
        return f"{self.__id} : {self.__name} : {self.__salary}"
        
    def display_details(self):
        print(f"Name : {self.__name}")
        print(f"Salary : {self.__salary}")
        print(f"id : {self.__id }")


    

class Developer(Employee):

    def calculate_bonous(self):
        bonous = self.get_salary() *(20/100)
        return bonous 

class Manager(Employee):
    def calculate_bonous(self):
        bonous = self.get_salary() *(35/100)
        return bonous 

class Intern(Employee):
    def calculate_bonous(self):
        bonous = 5000
        return bonous 

