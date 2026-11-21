
# 14. Multiple Inheritance Example

# Classes:

# Father
# Mother
# Child(Father, Mother)

# Access methods from both.

class Father:
    def __init__(self,name,age,surname):
        self.__name =name 
        self.__age = age
        self.__surname = surname
    
    
    def get_f_name (self):
        return self.__name
    
    
    def get_f_age(self):
        return self.__age

    
    def get_surname (self):
        return self.__surname
    
class Mother :
    
    def __init__(self,name ,age):
        self.__name = name 
        self.__age = age 
        
    def get_m_name (self):
        return self.__name
    
    def get_m_age(self):
        return self.__age


class Childeren(Father,Mother):
    def __init__(self,f_name,mother,surname,name, m_name,age):
        Father.__init__(f_name,surname)

        Mother.__init__(m_name)



        self.__name = name 
        self.__age = age 

    
    def details(self):
        mother_name = self.get_m_name()
        father_name = self.get_f_name()
        surname = self.get_surname()
        print(f"child's Name  : {self.__name} {surname} \nFather's Name : {father_name} \n Mother's Name : {mother_name} \nAge : {self.__age}")

f = Father("Dharmendra",47,"Vishnoi")
m = Mother("Laxmi",43)
c = Childeren("Kashish",20)
c.details()


# ask to sir 
