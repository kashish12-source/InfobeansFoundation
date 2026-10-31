# 2. Write a Java program to create a class called "Dog" with a name and breed attribute. Create two instances of the "Dog" class, set their attributes using the constructor and modify the attributes using the setter methods and print the updated values.

 
class Dog:
    def __init__(self , name , breed):
        self.__name = name 
        self.__breed = breed 
    
    def set_name(self,name):
        self._name = name

    def set_breed (self,breed):
        self.__breed = breed 

    def get_name(self):
        print(self._name)
    
    def get_breed (self):
        print(self.__breed)

    def display(self):
        print(f"Name of Dog is : {self.__name}")
        print(f"Breed of Dog is : {self.__breed}")
    

d1 = Dog("Tommy","Jerman Shefered")
d2 = Dog("Browno","Pomerian")
d1.display()
d2.display()
