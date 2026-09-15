salary = float(input("Enter the salary here :"))
service_year = int(input("Enter the Year of Services: "))

if(service_year>5):
    print(f"Bonus ammount is : {salary*0.05}")
else:
    print(f"Bonus is only for the employees servicing from more than 5 years ")