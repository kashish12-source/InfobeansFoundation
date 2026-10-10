# 56) WAP to print factorial of all the numbers between two entered numbers

num_1 = int(input("Enter the first no. here : "))
num_2 =int(input("Enter the second no. here : "))
for i in range(num_1,num_2+1):
    res = 1
    for j in range(2,i+1):
        res*=j
    print(f"factorial of no. {i} is {res}")