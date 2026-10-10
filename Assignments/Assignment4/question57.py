# 57) WAP to print all the prime numbers between two entered numbers

num_1 =int(input("Enter a first no. here : "))
num_2 =int(input("Enter the second no. here : "))

if num_1>1 and num_2 >1:
    print(f"the prime no. between {num_1} and {num_2} are : ")
    for i in range(num_1 , num_2+1):
        f= True
        for j in range(2,i):
            if(i%j==0):
                f=False
                break
        if(f):
            print(i,end = "   ")
else:
    print("Enter the no. greater than 1 ")