age1 = int (input ("Enter the age of First person: "))
age2 = int(input("Enter the age of Second Person: "))
age3 = int(input("Enter the age of third Person: "))

print(f"first person is eldest") if (age1>age2) and age1>age3 else print("second person is eldest")if age2>age3 else print("third person is eldest")

print("first person is youngest")if age1<age2 and age1<age3 else print("second person is youngest")if age2>age3 else print("Third person is youngest")
