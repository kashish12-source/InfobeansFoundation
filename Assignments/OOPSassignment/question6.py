# 6. Write a Java program to create a class called "Employee" with a name, job title, and salary attributes, and methods to calculate and update salary.

class Employee:
    def __init__(self , name, job_title, salary,present_days,year,month):
        self.__name = name
        self.__job_title = job_title
        self.__salary = salary
        self.__present_days =present_days
        self.__year =year
        self.__month = month

    def calculate_salary(self):
        
        days_30 = ['april', 'june','september','november']
        
        if (self.__month).lower() == 'febuary':
            if (self.__year %4 ==0 and self.__year %100 !=0)and self.__year%400==0:
                feb_days = 29
                salary_per_day = self.__salary //feb_days
                return self.__present_days*salary_per_day

            
            else:
                feb_days =28
                salary_per_day = self.__salary //feb_days
                return self.__present_days*salary_per_day

        elif self.__month in days_30:
            salary_per_day = self.__salary //30
            return self.__present_days*salary_per_day
        else:
            salary_per_day = self.__salary //31
            return self.__present_days*salary_per_day

    def update_salary(self,salary):
        
        print(f"salary is updated from {self.__salary} ",end="")
        self.__salary = salary
        print(f"to {self.__salary}")

    def get_salary(self):
        print(self.__salary)

    def display(self,calculated):
        print("____________________________Employee Details__________________________________")
    
        print(f"Name of Employee is : {self.__name}")

        print(f"Job Role of Employee is : {self.__job_title}")

        print(f"Salary if Employoee is : {self.__salary}")

        print(f"Present days of Employee is : {self.__present_days}")

        print(f"Salary given to the Employee is : {calculated}")

        print("______________________________________________________________________________")


e = Employee("kashish","CEO",345000,24,2025,"March")
calculated = e.calculate_salary()
e.display(calculated)
