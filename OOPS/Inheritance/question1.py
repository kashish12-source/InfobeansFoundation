class A :
    def __init__(self,name):
        self.__name = name 
    
    def get_name(self):
        return self.__name
    
class B(A):
    def greet(self):
        print(f'Good morning {self.get_name()}')

b = B("kashish")
b.greet()
