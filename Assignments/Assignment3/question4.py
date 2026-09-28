maths = float(input("enter the marks of maths:"))
science = float(input("enter the marks of science:"))
hindi = float(input("enter the marks of hindi:"))
english = float(input("enter the marks of english:"))
socialscience = float(input("enter the marks of social science:"))


total = maths + science + hindi + english + socialscience
percentage = total / 5

if percentage > 90 :
    print(f"MERIT and marks is : {percentage}")
elif percentage >= 60 and percentage <=90:
    print(f"A and marks is : {percentage}")
elif percentage >=50 and percentage <=59:
    print(f"B and marks is : {percentage}")
elif percentage >= 40 and percentage <=49:
    print(f"C and marks is : {percentage}")
elif percentage > 0 and percentage <=39:
    print(f"D and marks is : {percentage}")
    
else  :
    print("Invalid number ")