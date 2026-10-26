
# 7. Password Strength Checker
# Intermediate
# Concepts: Conditions, loops, functions, strings
# Requirements
# •	Accept a password from the user.
# •	Check its length.
# •	Check for uppercase and lowercase letters.
# •	Check for digits and special characters.
# •	Classify it as weak, medium, or strong according to your defined rules.
# Bonus: Display suggestions to improve a weak password.

def conditions(password):
   
    sc = lc = uc = dc = 0
    for i in password:
    
        if ord(i)>=65 and ord(i)<=90:
            uc+=1
        elif ord(i)>=97 and ord(i)<=122:
            lc+=1
        elif i.isdigit():
            dc+=1
        else:
            sc+=1

    
    length = len(password)

    if length < 8:
        print("Your password is weak: use at least 8 characters.")

    elif lc == 0 or uc == 0 or dc == 0 or sc == 0:
        print("Your password is weak.")

        if lc == 0:
            print("Add lowercase letters.")
        if uc == 0:
            print("Add uppercase letters.")
        if dc == 0:
            print("Add digits.")
        if sc == 0:
            print("Add special characters.")

    elif length >= 12 and lc >= 1 and uc >= 1 and dc >= 1 and sc >= 1:
        print("Your password is strong.")

    else:
        print("Your password is medium.")




password = input("Enter the password here : ")
conditions(password)