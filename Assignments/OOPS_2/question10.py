# 10. Company Department System
# Problem

# Create:

# Department
# Employee

# classes.

# Requirements

# Each department:

# has department name
# stores employee objects
# Functionalities
# Add employee to department
# Display all employees
# Calculate total department salary
# Concepts Practiced
# object composition
# object interaction
# storing objects in lists

class Department:
    def __init__(self,name ):
        self.__name = name
        self.__employees = []
    
    def add_employee(self,employee):
        self.__employees.append(employee)
        print("Employee added successfully")
    
    def display_details(self):
        print(f"Department : {self.__name}")
        for employee in self.__employees:
            print(f"Name:",employee.get_name())
            print("Contact : ", employee.get_contact())
            print("Salary" , employee.get_salary())



    def total_salary(self):
        total = 0
        for employee in self.__employees:
            total+=employee.get_salary()
        print(f"Total salary of the department is : {total}")
    


class Employee:
    def __init__(self, name ,salary,contact):
        self.__name = name 
        self.__contact = contact
        self.__salary = salary
    def get_name(self):
        return self.__name
    
    def get_contact(self):
        return self.__contact

    def get_salary(self):
        return self.__salary

e1 = Employee("Rahul",  9876543210, 30000)
e2 = Employee("Priya",  9876543211, 40000)
e3 = Employee("Aman",  9876543212, 35000)
d1 = Department("IT")
d1.add_employee(e1)
d1.add_employee(e2)
d1.add_employee(e3)
d1.display_details()
d1.total_salary()
