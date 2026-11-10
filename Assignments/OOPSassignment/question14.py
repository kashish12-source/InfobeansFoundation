# 14. Write a Java program to create a class called "School" with attributes for students, teachers, and classes, and methods to add and remove students and teachers, and to create classes.
class School :
    def __init__(self,students,teachers,classes):
        self.__students= students
        self.__teachers = teachers
        self.__classes = classes
    
    def add_teacher(self,quantity):
        self.__teacher+=quantity
        print("The teacher is added successfully")
    
    def remove_teacher(self,quantity):
        if quantity < self.__teachers:
            self.__teachers-=quantity
            print("The teacher are removed successfully")
        else:
            print("The quantity of teacher is already less ")
    
    def add_student(self, quantity):
        self.__students +=quantity
        print("Student added successfully")
    
    def remove_student(self,quantity):
        if quantity<self.__students:
            self.__students -= quantity
            print("Student are removed successfully")
        else:
            print("The quantity of teacher is already less ")
    
    def add_classes (self,quantity):
        self.__classes += quantity
        print("Classes added successfully")
    
    def remove_classes(self,quantity):
        if quantity<self.__classes:
            self.__classes -= quantity
            print("classes are removed successfully")
        else:
            print("The quantity of classes is already less ")
    
    def display(self):
        print(f"The no. of students is : {self.__students}")
        print(f"The no. of teachers is : {self.__teachers}")
        print(f"The no. of classes is : {self.__classes}")
    
s = School(20,23,1)
s.add_classes(3)
s.display()
s.add_student(24)
s.remove_teacher(22)
s.display() 