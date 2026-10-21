#  Check whether the key "age" exists in a dictionary
students = {"name":"kashish","branch":"CSE","contact":7489619180}
for key in students.keys():
    if key =="age":
        print("yes age is present as a key in the dictionary")
        break
else:
    print("No age is not present as a key in the dictionary ")
