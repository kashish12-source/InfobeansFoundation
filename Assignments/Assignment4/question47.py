# 47) WAP to print tables of all the numbers between two entered numbers
num_1 = int(input("Enter 1st no. : "))

num_2 =int(input("Enter 2nd no. : "))

for i in range(num_1,num_2+1):
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")
    print()
    