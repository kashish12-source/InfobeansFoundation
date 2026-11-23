
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
    
    
    def get_f_details(self):
        return self.__name,self.__age,self.__surname

    
class Mother :
    
    def __init__(self,m_name ,m_age):
        self.__m_name = m_name 
        self.__m_age = m_age 
        
    def get_m_details(self):
        return self.__m_age,self.__m_name


class Children(Father,Mother):
    def __init__(self,f_name,f_age,f_surname,m_name,m_age,c_name,c_age):
        # super().__init__(f_name,f_age,f_surname)
        # super().__init__(m_name,m_age)
        Father.__init__(self,f_name,f_age,f_surname)
        Mother.__init__(self,m_name,m_age)
        
        self.__name = c_name 
        self.__age = c_age 

    def display(self):
        f_name ,f_age,f_surname = self.get_f_details()
        m_age,m_name = self.get_m_details()
        print(f"Father's Name : {f_name} {f_surname}")

        print(f"Mother's Name : {m_name} {f_surname }")

        print(f"Child's Name : {self.__name} {f_surname}")

        print(f"Child's age : {self.__age}")

c = Children("Dharmendra",47,"Vishnoi","Laxmi",45,"Kashish",20)
c.display()


