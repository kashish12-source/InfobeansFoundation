salary = int(input('Enter the salary here : '))

if salary <=10000:
    hra = salary *0.2
    da = salary *0.80
elif salary <=20000:
    hra = salary *0.25
    da = salary *0.9
elif salary >20000 :
    hra = salary * 0.3
    da = salary * 0.95
else:
    print("please enter the salary properly ")

print(f"the gross employee salary is : {salary + hra+da}")
