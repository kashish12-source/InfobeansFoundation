# 8. Employee Attendance and Salary Calculator
# Intermediate
# Concepts: Conditions, loops, functions, dictionaries
# Requirements
# •	Enter employee details and days present.
# •	Calculate attendance percentage.
# •	Calculate salary based on days worked.
# •	Apply a bonus or deduction according to attendance rules.
# •	Generate an employee summary.



def Details():
    name = input("Enter the name of the employee here : ")
    age = int(input("Enter the age of the employee here : "))
    if not 60>=age>=18:
        print("Enter the age between the age 18 to 60")
        return 

    branch = input("Enter the branch of the employee here : ")
    month = int(input("Enter the no. of month "))
    if not 12>=month>=1:
        print("Enter the valid month")
        return

    year = int(input("Enter a year here : "))
    if not 2000<=year<=2026:
        print("Enter valid year")
        return

    days_present = int(input("Enter a no. of days employee is present : "))
    if not 1<=days_present<=30:
        print("Enter the valid no. of days ")
        return


    return name ,age ,branch,month,year,days_present

def calculate_attendance_per(days,month,year):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month ==10 or month == 12:
        percentage= ((days/31)*100)
    elif month == 2 and ((year%4 ==0 and year%100 !=0)or year%400 ==0 ):
        percentage= ((days/29)*100)
    elif month == 2 :
        percentage= ((days/28)*100)
    else:
        percentage = ((days/30)*100)
    return percentage
def calculate_salary(percentage):
    if percentage >=90:
        return 900000
    elif percentage >=80 and percentage<90:
        return 800000
    elif percentage>=70 and percentage<80:
        return 700000
    elif percentage>=60 and percentage<70:
        return 650000
    else :
        return 40000
def calculate_bonous(percentage):
    
    if percentage >90 :
        return 10000
    elif 90>percentage>=80:
        return 8000
    elif 80>percentage>=70:
        return 50000 
    else :
        return -40000

name , age ,branch,month,year,days_present = Details()
attendence = calculate_attendance_per(days_present,month,year)
salary = calculate_salary(attendence)
bonous = calculate_bonous(attendence)



print("_______________________________________________SUMMARY OF EMPLOYEE______________________________________________")
print(f"\nNAME : {name.upper()}")
print(f"\nAGE : {age}")
print(f"\nBRANCH : {branch.upper()}")
print(f"\nMONTH : {month}")
print(f"\nYEAR : {year}")
print(f"\nDAYS : {days_present}")
print("\n")
print(f"ATTENDENCE PERCENTAGE : {attendence}")
print()
print(f"SALARY : {salary}")
print()
if bonous < 0:
    print(f"DEDUCTION : {bonous}")
    salary =salary-bonous
else:
    print(f"BONOUS : {bonous}")
    salary =salary + bonous
print()
print(f"FINAL SALARY IS : {salary}")

print()

print("__________________________________________________________________________________________________________________")



    