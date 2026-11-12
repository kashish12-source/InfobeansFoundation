class A :
    def __init__(self,name):
        self.__name = name 

    def get_name(self):
        return self.__name
    

class B(A):
    def __init__(self,name,age):
        super().__init__(name)

        self.__age = age
    
    def get_age(self):
        return self.__age
    
class C(B):
    def details(self):
        print(f"Name of the student is {self.get_name()} and he is of {self.get_age()} years old")

c = C("kashish", 20)
c.details()