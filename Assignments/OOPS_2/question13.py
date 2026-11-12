# Problem

# Create exam management system.

# Requirements

# Each exam object:

# exam name
# total marks
# passing marks
# Functionalities
# Check pass/fail
# Calculate grade
# Maintain total exams conducted


class Exam:
    __total_exams = 0

    def __init__(self, exam_name, total_marks, passing_marks):
        self.__exam_name = exam_name
        self.__total_marks = total_marks
        self.__passing_marks = passing_marks
        Exam.__total_exams += 1

    def check_result(self, obtained_marks):
        if obtained_marks >= self.__passing_marks:
            print("Result: Pass")
        else:
            print("Result: Fail")

    def calculate_grade(self, obtained_marks):
        if obtained_marks >= self.__total_marks * 0.90:
            grade = "A"

        elif obtained_marks >= self.__total_marks * 0.75:
            grade = "B"

        elif obtained_marks >= self.__total_marks * 0.50:
            grade = "C"

        elif obtained_marks >= self.__passing_marks:
            grade = "D"

        else:
            grade = "F"

        print("Grade:", grade)
    @classmethod
    def total_exams(cls):
        print("Total exams conducted:", cls.__total_exams)


e1 = Exam("Python", 100, 35)
e2 = Exam("Java", 100, 40)
e3 = Exam("DBMS", 100, 35)



marks = int(input("Enter obtained marks in Python: "))

e1.check_result(marks)
e1.calculate_grade(marks)

Exam.total_exams()
