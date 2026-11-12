class A:
    def __init__(self, name ):
        self.__name = name 

    def get_name (self):
        return self.__name

class B:
    def __init__(self,age):
        self.__age = age 
    
    def get_age(self):
        return self.__age
    
class C(A(B)):
    