percentage = 40

match percentage:
    case percentage if percentage>90: print("Grade A")
    case percentage if percentage>=80 and percentage<=90 : print("Grade B")
    case percentage if percentage >=60 and percentage<80 : print("Grade C")
    case _:print("Grade D ")
