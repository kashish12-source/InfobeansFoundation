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



class Exam :
    total = 0
    def __init__(self, name , total_marks,passing_marsk):
        self.__name = name
        self.__total_marks = total_marks
        self.__passing_marks = passing_marsk
        Exam.total+=1
    
    def result(self,marks):
        # marks = float(input("Enter the marks you have obtained here : "))
        if marks > self.__passing_marks and marks < self.__total_marks:
            print("You have passed this exam")
        else:
            print("You are fail in this exam ")
    
    def grade(self,marks):
        # marks = float(self.result())
        percentage = (marks /float(self.__total_marks))*100

        if percentage >90:
            print("Garde is : A")
        elif 80<=percentage <=90:
            print("Grade is : B")
        elif 70<=percentage<80:
            print("Grade is : C")
        elif 60<=percentage<70:
            print("Grade is : D")
        else:
            print("Grade is : E")

    @classmethod
    def display_exams(cls):
        print(f"Total exams held is : {cls.total}")



e1 = Exam("Python", 100, 35)
e2 = Exam("Java", 100, 40)
e3 = Exam("DBMS", 100, 35)



marks = int(input("Enter obtained marks in Python: "))

e1.result(marks)
e1.grade(marks)

Exam.total_exams()



























# class Exam:
#     __total_exams = 0

#     def __init__(self, exam_name, total_marks, passing_marks):
#         self.__exam_name = exam_name
#         self.__total_marks = total_marks
#         self.__passing_marks = passing_marks
#         Exam.__total_exams += 1

#     def check_result(self, obtained_marks):
#         if obtained_marks >= self.__passing_marks:
#             print("Result: Pass")
#         else:
#             print("Result: Fail")

#     def calculate_grade(self, obtained_marks):
#         if obtained_marks >= self.__total_marks * 0.90:
#             grade = "A"

#         elif obtained_marks >= self.__total_marks * 0.75:
#             grade = "B"

#         elif obtained_marks >= self.__total_marks * 0.50:
#             grade = "C"

#         elif obtained_marks >= self.__passing_marks:
#             grade = "D"

#         else:
#             grade = "F"

#         print("Grade:", grade)
#     @classmethod
#     def total_exams(cls):
#         print("Total exams conducted:", cls.__total_exams)


# e1 = Exam("Python", 100, 35)
# e2 = Exam("Java", 100, 40)
# e3 = Exam("DBMS", 100, 35)



# marks = int(input("Enter obtained marks in Python: "))

# e1.check_result(marks)
# e1.calculate_grade(marks)

# Exam.total_exams()
