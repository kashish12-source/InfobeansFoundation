# 6. Write a Java program to create a class called "Employee" with a name, job title, and salary attributes, and methods to calculate and update salary.

class Employee:
    def __init__(self , name, job_title, salary):
        self.__name = name
        self.__job_title = job_title
        self.__salary = salary
    
    