# company hierarchy 
# person - employee(person)
# manager(employee)
# display company hierarchy 

class Person:
    def __init__(self,name,age,address):
        self.__name = name 
        self.__age = age 
        self.__address = address
    
    def person_details(self):
        return self.__name , self.__age , self.__address
    
class Employee(Person):
    def __init__(self,name,age,address,contact,e_id):
        super().__init__(name,age,address)
        self.__contact = contact 
        self.__e_id = e_id
    
    def employee_details(self):
        return self.__contact , self.__e_id

class Manager(Employee):
    def __init__(self,name,age,address,contact,e_id ,department,experience):
        super().__init__(name,age,address,contact,e_id)
        self.__department =department
        self.__salary = experience
    
    def details(self):
        print("_____________DETAIL_____________")
        name ,age, address = self.person_details()
        contact , e_id = self.employee_details()
        print(f"NAME : {name}\nAGE: {age}\nADDRESS : {address}\nCONTACT : {contact}\nID : {e_id}\nDEPARTMENT : {self.__department}\nSALARY : {self.__salary}")
        print("________________________________")

m = Manager("kashish",20,"prajapat nagar",93425324,101,"CEO",3)
m.details()
        