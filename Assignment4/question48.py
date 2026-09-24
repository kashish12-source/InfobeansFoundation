# 48) WAP to find out the factors of all the numbers between two entered numbers

num_1 = int(input("Enter 1st no. : "))

num_2 =int(input("Enter 2nd no. : "))

for i in range(num_1, num_2+1):
    print(f"factors of number {i} is : ",end="  ")
    for j in range(1,(i//2)+1):
        if(i%j==0):
            print(j,end=" ")
    print()