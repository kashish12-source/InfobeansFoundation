# 10. Write a Java program to create a class called "Student" with a name, grade, and courses attributes, and methods to add and remove courses.
class Student:
    def __init__(self,name,grade,*courses):
        self.__name = name 
        self.__grade = grade
        self.__course = list(courses)
    
    def add_course(self,course):

        self.__course.append(course)
        print("course added successfully ")

    
    def remove_course(self,course):
        if course in self.__course:
            self.__course.remove(course)
            print("course removed successfully")

        else:
            print("The course is not present")

    def display(self):
        print(f"name : {self.__name}")
        print(f"grade : {self.__grade}")
        print(f"courses : {self.__course}")

s1 = Student("kashish",5,"english","hindi","maths","science")
s1.display()
s1.add_course("geometry")
s1.display()
s1.remove_course("hindi")
s1.display()