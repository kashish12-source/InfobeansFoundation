# 17. Online Course Platform
# Course
# ProgrammingCourse
# PythonCourse

# Add certification system.


class Course:
    def __init__(self, c_name,c_id ,c_price):
        self.__c_name = c_name
        self.__c_id = c_id
        self.__c_price = c_price
    
    def get_details(self):
        return self.__c_id,self.__c_price,self.__c_name

    

class ProgrammingCourses:

    def __init__(self):
        self.__courses = {}
    
    def add_course(self,course):
        course_id = course.get_details()[0]
        self.__courses[course_id] =course

    def chec_id(self,id):
        if id in self.__courses.keys():
            return True
        else:
            return False
    
    def display_courses(self):
        for course in self.__courses.values():
            print(course.get_details())

class ChooseAndPay(ProgrammingCourses):
    def __init__(self):
        id = int(input("Enter the Id of the course you want to purchase: "))
        if  self.chec_id(id):
            amount = int(input("Enter the amount here : "))
            if amount == self.chec_id(id)["price"]:
                print("Payment is successful")
            else:
                print("Enter the valid amount ")
        else:
            print("Course not found ")
    

course_repo = ProgrammingCourses()

c1 = Course("Python",101,15000)
c2 = Course("Java ", 102,12399)

course_repo.add_course(c1)
course_repo.add_course(c2)

course_repo.display_courses()



























































































































# class Course : 
    
#     __course_collection = {}

#     def __init__(self,course_name ,course_id,course_duration,course_price,course_type):
#         self.__course_name = course_name
#         self.__course_id = course_id
#         self.__course_duration = course_duration
#         self.__course_price = course_price
#         self.__course_type = course_type

#         Course.__course_collection[course_id] = {"course name": self.__course_name , "course duration" :self.__course_duration, "course price":self.__course_price , "course type":self.__course_type}


    
#     def display_all_courses(self):
#         print()
#         for key ,val in Course.__course_collection.items():
#             print(f"Couser ID : {key} - Details : {str(val)}")

#         print()
    
#     def get_course_details(self):
#         return self.__course_name,self.__course_id,self.__course_duration,self.__course_price,self.__course_type
   


# class ProgrammingCourse(Course):
    

#     def __init__(self):
#         self.display_all_courses()

#     def choose_course(self):
#         id= int(input("Enter the ID of the course here : "))
#         if id in Course._Course__course_collection:
#             print("Course has been selected successfully")

#             return id
        
#         else:

#             print("Course not found ")
#             return None

#     def payment(self,course_id):
            
#             amount = Course._Course__course_collection[course_id]["course price"]
#             print(f"If you want to purchase a course you have to pay : {amount}")
#             print("Press 1 to continue to payment \nPress 2 to leave the site ")
#             choice= int(input("\nEnter your choice here : "))
#             if choice == 1:
#                 print("Payment successfull")
#                 return True
#             elif choice == 2:
#                 print("Payment cancled ")
#                 return False
#             else:
#                 print('Enter a valid no. ')
#                 return False
    
#     def get_duration(self,course_id):
        
#         if course_id is not None :
#             return Course._Course__course_collection[course_id]["course duration"]

# class PythonCertification(ProgrammingCourse):

#     def __init__(self,s_name,institute):
#         super().__init__()


#         self.__name = s_name
        
#         self.__institute = institute

#     def certifcation (self):
#         course_id = self.choose_course()
#         if course_id is None:
#             return 
#         self.__duration = self.get_duration(course_id)

#         if self.payment(course_id):
#             print("_____________________CONGRATULATIONS____________________")
#             print(f'''This credential is awarded to {self.__name } from {self.__institute} \nfor successfully completed the tranning of {self.__duration} months on \n\t python programming ''')
#             print("_________________________________________________________")
            

# c1 = Course("Python", 101, 3, 5000, "Programming")
# c2 = Course("Java", 102, 4, 6000, "Programming")
# c3 = Course("C++", 103, 2, 3000, "Programming")

# p = PythonCertification("kashish","IIST")
# p.certifcation()






        

