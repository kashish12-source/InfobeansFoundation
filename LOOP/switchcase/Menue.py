while True:
    print("Press 1 for addition:")
    print("Press 2 for substraction")
    print("Press 3 for multiplication")
    print("press E/e for termination or exit ")
    n = int(input("enter the no"))


    match n:
        case 1:
            a = float(input("enter 1st value"))
            b= float(input ("enter 2nd value"))
            print(f"addition is {a+b}")

        case 2: 
            a =float (input("enter 1st value"))
            b= float(input ("enter 2nd value"))
            print(f"substraction is {a-b}")
        case 3: 
            a = float(input("enter 1st value"))
            b= float(input ("enter 2nd value"))
            print(f"multiplication is {a*b}")
        case "E"|"e":
            break
        case _:
            print("invalid no. ")