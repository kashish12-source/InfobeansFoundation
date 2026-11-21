# 12. University System
# Person
# Student(Person)
# GraduateStudent(Student)

# Add thesis information.



class Person:
    def __init__(self, name , age ,address ,gender):
        self.__name = name 
        self.__age = age 
        self.__address = address
        self.__gender = gender 

    def person_details(self):
        return self.__name ,self.__age , self.__address ,self.__gender 


class Student(Person):
    def __init__(self,name ,age,address,gender,branch,id):
        super().__init__(name,age,address,gender)
        self.__branch = branch
        self.__id = id 

    def student_details(self):
        return self.__branch , self.__id

class GraduateStudent(Student):
    
    def __init__(self, name ,age, address ,gender , branch ,id , certification ,duration ):
        super().__init__(name ,age ,address,gender, branch,id)
        self.__certification = certification
        self.__duration = duration

    def display(self):
        name,age,address,gender = self.person_details()
        branch,id = self.student_details()
        print("___________DETAILS__________")
        print(f"NAME : {name}\nAGE: {age} \nADDRESS : {address}\nGENDER :{gender} \nBRANCH : {branch} \nID : {id} \nCERTIFICATION : {self.__certification} \nDURATION : {self.__duration} months")

        print("____________________________")
        

gs = GraduateStudent("kashish",20,"Prajapat nagar","Female","CSE",101,"Python certification",5)
gs.display()


