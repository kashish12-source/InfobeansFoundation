# 6. Hospital Management

# Parent:

# HospitalStaff

# Child:

# Doctor
# Nurse
# Receptionist

# Implement duties().

from abc import ABC , abstractmethod

class HospitalStaff(ABC):
    @abstractmethod
    def details(self):
        pass 
    
    @abstractmethod
    def work(self):
        pass 


class Doctor(HospitalStaff):

    def __init__(self,name ,age,speciality,salary,timing):
        self.__name = name 
        self.__age = age 
        self.__specicality = speciality
        self.__salary = salary 
        self.__timing = timing 

    
    def details(self):
        print("__________________________DETAILS OF DOCTOR _______________________")
        print(f"Name : {self.__name}\nAge : {self.__age}\nSpeciality : {self.__specicality}\nSalary : {self.__salary} \nTime : {self.__timing}")
        print("___________________________________________________________________")

    def work(self):
        print("He saw the patients in the hospital in genral ward \n")

class Nurse(HospitalStaff):
    def __init__(self, name ,age ,section):
        self.__name = name 
        self.__age = age 
        self.__section = section

    def details (self):
        print("___________________________DETAILS OF NURSE________________________")
        print(f"Name : {self.__name }\nAge : {self.__age}\nSection : {self.__section}\n")
        print("___________________________________________________________________\n")
    
    def work(self):
        print("Nurse works with the doctore for the side work of the paitent \n")

class Receptionist(HospitalStaff):
    def __init__(self, name ,age ,contact , salary):
        self.__name = name 
        self.__age = age 
        self.__contact = contact 
        self.__salary = salary

    def details (self):
        print("_____________DETAILS OF THE RECEPTIONIST_______________")
        print(f"Name : {self.__name}\nAge : {self.__age}\nContact : { self.__contact} \nSalary : {self.__salary}")
        print("_______________________________________________________\n")
    
    def work(self):
        print("work to solve the queries of the attenders and enert the details of the paitent ")

d1 = Doctor("Kashish", 20,"Neurologist" ,2000000,"7:30")
n1 = Nurse("kavya" , 25,"Neuro")
r1 = Receptionist("Guatam",30,5479563056,21000)
d1.details()
d1.work()
n1.details()
n1.work()
r1.details()
r1.work()



