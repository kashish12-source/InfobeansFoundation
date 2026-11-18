# 4. Student Management

# Base class Person.

# Derived:

# Student
# Teacher

# Add role-specific methods.

class Person:
    def __init__(self, name, age, contact, address, adhar):
        self.__name = name
        self.__age = age
        self.__contact = contact
        self.__address = address
        self.__adhar = adhar

    def get_details(self):
        print(f"NAME : {self.__name}")
        print(f"AGE : {self.__age}")
        print(f"CONTACT : {self.__contact}")
        print(f"ADDRESS : {self.__address}")
        print(f"ADHAR : {self.__adhar}")


class Student(Person):

    def details(self):
        self.__classes = int(input("Enter your class here: "))
        self.__section = input("Enter your section here: ")

        print("____________STUDENT DETAILS____________")

        super().get_details()

        print(f"STANDARD : {self.__classes}")
        print(f"SECTION : {self.__section}")

        print("________________END________________")


class Teacher(Person):

    def details(self):
        self.__salary = int(input("Enter your salary here: "))
        self.__years = int(input("Enter your years of experience: "))

        print("____________TEACHER DETAILS____________")

        super().get_details()

        print(f"SALARY : {self.__salary}")
        print(f"EXPERIENCE : {self.__years} years")

        print("________________END________________")


# Creating objects

s = Student("Kashish", 20, 7489619180, "Indore", 23426424553)
t = Teacher("Rahul", 35, 9876543210, "Bhopal", 12345678901)

s.details()
t.details()
