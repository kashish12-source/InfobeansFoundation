# 18. School Classroom System
# Problem

# Create classroom system.

# Requirements

# Classroom should:

# maintain student objects
# maintain class teacher
# Functionalities
# Add student
# Remove student
# Display class strength
# Concepts Practiced
# object aggregation
# collections of objects


class Student:
    def __init__(self, name, roll_no, age):
        self.__name = name
        self.__roll_no = roll_no
        self.__age = age

    def display_student(self):
        print("Name:", self.__name)
        print("Roll Number:", self.__roll_no)
        print("Age:", self.__age)


class Classroom:
    def __init__(self, class_name, teacher):
        self.__class_name = class_name
        self.__teacher = teacher
        self.__students = []

    def add_student(self, student):
        self.__students.append(student)
        print("Student added successfully")

    def remove_student(self, roll_no):
        for student in self.__students:
            if student._Student__roll_no == roll_no:
                self.__students.remove(student)
                print("Student removed successfully")
                return

        print("Student not found")

    def display_students(self):
        print("\nClass:", self.__class_name)
        print("Class Teacher:", self.__teacher)

        print("\nStudent Details:")

        for student in self.__students:
            student.display_student()

    def class_strength(self):
        print("Total students:", len(self.__students))


s1 = Student("Rahul", 101, 15)
s2 = Student("Priya", 102, 16)
s3 = Student("Aman", 103, 15)
s4 = Student("Sneha", 104, 16)

c1 = Classroom("10th A", "Mr. Sharma")

c1.add_student(s1)
c1.add_student(s2)
c1.add_student(s3)
c1.add_student(s4)

c1.display_students()

c1.class_strength()

print("\nRemoving student")

c1.remove_student(102)

c1.class_strength()
