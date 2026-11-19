# company hierarchy 
# person - employee(person)
# manager(employee)
# display company hierarchy 


class Person:
    __details = {}
    def __init__(self,id, name , age ,contact ,address ,position, salary):
        self.__id = id 
        self.__name =name
        self.__age = age
        self.__address = address
        self.__position = position
        self.__salary = salary
        self.__contact=contact

        Person.__details[id] = {"name" :self.__name, "age":self.__age,"contact":self.__contact,"address":self.__address , "position": self.__position, "salary":salary}
    def display(self):
        print("___________________Details of Employee___________________")
        print(f"NAME : {super().self.__name}\nID : {super().self.__id}\nAGE : {super().self.__age}\nADDRESS : {super().self.__address}\nPOSITION : {super().self.__position}\nSALARY : {super().self.__salary}\nCONTACT : {super().self.__contact}")


class Employee(Person):
    
    def display(self):
        print("___________________Details of Employee___________________")
        print(f"NAME : {super().self.__name}\nID : {super().self.__id}\nAGE : {super().self.__age}\nADDRESS : {super().self.__address}\nPOSITION : {super().self.__position}\nSALARY : {super().self.__salary}\nCONTACT : {super().self.__contact}")
    

class Manager(Employee):
    __project_details ={}

    Employee.detail()
    Employee.display()
    def projects (self):
        id = int(input("Enter the ID of the manager here : "))
        if id in Person.__details:
            project_name = input("Enter the name of the project ")
            Manager.__project_details[id] = project_name 
            print("Project has been added in the managers account")
        else:
            print("Manger is not peresent their")
    def display_project(self):
        for key , val in Manager.__project_details.items():
            print(f"{key} = {val}")



p1 = Person(101,"kashish",20,7489619180,"388 - c prajapat nagar ", "HR", 240000)
p2 = Person(102,"keshav",23,7489619143,"38 - D vijay nagar ", "TPO", 23400)
p3 =Person(103,"piyush",24,7489614580,"34 - e sudama nagar ", "CTO", 23450)
p1.display()
p2.display()

