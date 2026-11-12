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

class Employee:
    def __init__(self, name, age, contact, salary):
        self.name = name
        self.age = age
        self.contact = contact
        self.salary = salary


class Department:
    def __init__(self, name):
        self.__name = name
        self.__employees = []

    # Add employee
    def add_employee(self, employee):
        self.__employees.append(employee)
        print("Employee added successfully")

    # Display all employees
    def display_employees(self):
        print(f"\nDepartment: {self.__name}")

        for employee in self.__employees:
            print("Name:", employee.name)
            print("Age:", employee.age)
            print("Contact:", employee.contact)
            print("Salary:", employee.salary)
            print("--------------------")

    # Calculate total department salary
    def total_salary(self):
        total = 0

        for employee in self.__employees:
            total += employee.salary

        print("Total Department Salary:", total)


# Creating employee objects

e1 = Employee("Rahul", 24, 9876543210, 30000)
e2 = Employee("Priya", 25, 9876543211, 40000)
e3 = Employee("Aman", 23, 9876543212, 35000)


# Creating department object

d1 = Department("IT")

# Adding employees to department

d1.add_employee(e1)
d1.add_employee(e2)
d1.add_employee(e3)

# Display employees

d1.display_employees()

# Calculate total salary

d1.total_salary()
