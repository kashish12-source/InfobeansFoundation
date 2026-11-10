
# 4. Student Grade System
# Problem

# Create a student result management system.

# Requirements

# Each student should have:

# roll number
# name
# marks in 3 subjects
# Functionalities
# Calculate total marks
# Calculate percentage
# Assign grade:
# A → 90+
# B → 75+
# C → 50+
# Fail otherwise
# Track total students
# Concepts Practiced
# instance methods
# conditional logic in classes
# object-based calculations

class Student:
    total_students = 0
    def __init__(self, rollno ,name, hindi,english,maths):
        self.__rollno = rollno
        self.__hindi = hindi
        self.__english = english
        self.__name  = name 
        self.__maths = maths
        Student.total_students +=1

    def total_marks (self):
        marks = self.__hindi + self.__english + self.__maths 

        print(f"Total marks of {self.__name} is : {marks}")
        return marks
    
    def percentage (self):
        percentage = self.total_marks()/3
        return percentage
    
    def grade(self):
        if self.percentage()>=90:
            print(f"Grade of {self.__name} is : A")
        elif 90>self.percentage()>=75:
            print(f"Grade of {self.__name} is : B")
        elif 75>self.percentage()>=50:
            print(f"Grade of {self.__name} is : C")
        else:
            print(f"Student {self.__name} is fail")
            
    @classmethod
    def display_student_count(cls):
        print(f"Total no. of students are : {Student.total_students}")


    
s1 =Student(101,"kashish",89,86,83)
s2 = Student(102,"keshav",98,78,86)
s3 = Student(103,"piyush",99,56,86)
s1.total_marks()
s2.percentage()
s3.grade()

Student.display_student_count()
