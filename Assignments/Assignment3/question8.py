classes_held = int (input ("enter the no. of classes held : "))

classes_attended = int(input ("enter the no. of classes attended : "))

per = (classes_attended/classes_held)*100

if per>=75:
    print(f"the student is allowed to sit in the exam : {per}")
else:
    print(f"the student is not allowed to sit int the exam : {per}")
    medical = input('Enter yes if any medical case or no for the not the medical case : ')
    if medical == "yes":
        print("student is allowed to sit in the exam")
    else:
        print("student is not allowed to sit in the exam")