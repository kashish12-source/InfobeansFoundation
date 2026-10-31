# 9. Write a Java program to create a class called "Employee" with a name, salary, and hire date attributes, and a method to calculate years of service.
from datetime import datetime
class Employee:
    def __init__(self, name ,salary , month , year):
        self.__name = name 
        self.__salary = salary
        self.__month = month 
        self.__year = year
    
    def calculate_years(self):
        current_year = datetime.now().year
        current_month = datetime.now().month
        if self.__year>current_year:
            return False
        else:
            years = current_year - self.__year
            if self.__month > current_month:
                years -=1
            return years
e1 = Employee("kashish",2300000,12,2024)
if e1.calculate_years():
    print(f"No. of years is : {e1.calculate_years()}")
else:
    print("please Enter a valid year")
