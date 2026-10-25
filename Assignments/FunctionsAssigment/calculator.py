# 1. Smart Calculator
# Beginner
# Concepts: if-elif-else, while, functions
# Requirements
# •	Display a menu for addition, subtraction, multiplication, division, and modulus.
# •	Take two numbers from the user.
# •	Use separate functions for each operation.
# •	Handle division by zero.
# •	Repeat until the user selects Exit.
# Bonus: Add power and floor division operations.


def addition(x,y):
    return x+y

def substraction(x,y):
    return x-y 

def multiplication(x,y):
    return x*y

def division(num,deno):
    if deno == 0:
        return False
    else:
        return num / deno
    
def modulo(num , deno):
    if deno == 0:
        return False
    else:
        return num % deno

def power(num,pow):
    return num ** pow

def floorDivision(num,deno):
    if deno == 0:
        return False
    else:
        return num // deno

f =True
while(f):
    print("Press 1 for addition ")
    print("Press 2 for substraction ")
    print("Press 3 for multiplication ")
    print("Press 4 for division ")
    print("Press 5 for floor division ")
    print("Press 6 for modulous ")
    print("Press 7 for power ")
    print("Press 8 for exit ")
    print()
    inputs = int(input("Enter your choice "))
    print()

    if(inputs == 1):
        num1 = int(input("Enter first no.: "))
        num2 = int(input("Enter second no.: "))
        print()
        print(f"The sum of the two no. {num1} and {num2} is : {addition(num1,num2)}")
        print()
    elif(inputs == 2):
        num1 = int(input("Enter first no.: "))
        num2 = int(input("Enter second no.: "))
        print()
        print(f"The substraction of the two no. {num1} and {num2} is : {substraction(num1,num2)}")
        print()
    elif(inputs == 3):
        num1 = int(input("Enter first no.: "))
        num2 = int(input("Enter second no.: "))
        print()
        print(f"The multiplication of the two no. {num1} and {num2} is : {multiplication(num1,num2)}")
        print()
    elif(inputs == 4):
        num1 = int(input("Enter first no.: "))
        num2 = int(input("Enter second no.: "))
        print()
        if division(num1,num2):
            print(f"The  of the division no. {num1} and {num2} is : {division(num1,num2)}")
            print()
        else:
            print("Division by  0 is not possible ")
            print()
    elif(inputs == 5):
        num1 = int(input("Enter first no.: "))
        num2 = int(input("Enter second no.: "))
        print()
        if floorDivision(num1,num2):
            print(f"The floor division of the two no. {num1} and {num2} is : {floorDivision(num1,num2)}")
            print()
        else :
            print("Floor division by 0 is not possible")
            print()
    elif(inputs == 6):
        num1 = int(input("Enter first no.: "))
        num2 = int(input("Enter second no.: "))
        print()
        if modulo(num1,num2):
            print(f"The modulous of the two no. {num1} and {num2} is : {modulo(num1,num2)}")
            print()
        else :
            print("modulous by 0 is not possible")
            print()
    elif inputs ==7:
        num1 = int(input("Enter the first no. : "))
        num2 = int(input("Enter the power no. : "))
        print()
        print(f"The result is : {power(num1,num2)}")
        print()
    elif inputs == 8:
        f = False
    
    else:
        print("Invalid choice please choose properly")
        print()

print()
print()