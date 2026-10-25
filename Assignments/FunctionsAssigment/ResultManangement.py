# 2. Student Result Management System
# Beginner
# Concepts: Conditions, loops, functions
# Requirements
# •	Input marks for five subjects.
# •	Calculate total, percentage, and grade.
# •	Check whether the student passed or failed.
# •	Validate that each mark is between 0 and 100.
# •	Create functions such as calculate_total(), calculate_percentage(), and calculate_grade().
# Bonus: Accept results for multiple students and calculate the class average.

def calculate_total(maths,science,english ,hindi, social):
    return maths+science+english+hindi+social
def calculate_percentage(total):
    return total/5
def calculate_grade(percentage):
    if percentage >=90:
        print ("A")
    elif percentage >=80 and percentage<90:
        print("B")
    elif percentage >=70 and percentage<80:
        print("C")
    elif(percentage >=60 and percentage<70):
        print("D")
    else:
        print("Fail")


def TakeInput(num):
    if num == 1:
        maths = float(input("Enter marks of maths : "))
        science=float(input("Enter marks of science : "))
        english = float(input("Enter marks of English : "))
        hindi = float(input("Enter marks of Hindi : "))
        socialscience = float(input("Enter marks of social science : "))
        total = calculate_total(maths , science,english,hindi,socialscience)
        percentage = calculate_percentage(total)
        print()
        print(f"Total marks of the student is : {total}")
        print(f"The percentage of the student is : {percentage}")
        print("The grade of the student is : ",end="")
        calculate_grade(percentage)
        print()



        
def TakeInputs(n):
        students =n
        j=1
        l = []
        while(n!=0):
            
            maths = float(input("Enter marks of maths : "))
            science=float(input("Enter marks of science : "))
            english = float(input("Enter marks of English : "))
            hindi = float(input("Enter marks of Hindi : "))
            socialscience = float(input("Enter marks of social science : "))
            print()

            total = calculate_total(maths , science,english,hindi,socialscience)
            percentage = calculate_percentage(total)
            l.append(total)

            print(f"The marks of the student {j} is {total} ")
            print(f"The percentage of the student {j} is : {percentage}")
            print(f"The grade of the student {j} is : ",end="")
            calculate_grade(percentage)
            print()

            j+=1

            n-=1
        print()
        sum =0
        for i in l:
            
            sum+=i
        print(f"The average of the class is : {sum / students:.2f}")


print("Press 1 to enter only one student's marks ")
print("Press 2 to enter more than 1 student's marks ")
print()

num = int(input("Enter your choice here : "))
if num== 1 or num==2:
    if num == 1:
        TakeInput(num)
    else:
        n = int(input("Enter the no. of students: "))
        TakeInputs(n)
else:
    print("Enter the valid no. ")

print()




