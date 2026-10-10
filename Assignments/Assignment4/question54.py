# 54) WAP to print all the even numbers between two entered numbers
num_1 = int(input("Enter the first no. here : "))
num_2 = int(input("Enter the second no. here : "))
if num_1>0 and num_2>0:
    print(f"All the even no. between {num_1} and {num_2} are")
    for i in range(num_1,num_2+1):
        if(i%2==0):
            print(i,end="  ")
else:
    print("enter the no. greater than 0 as 0 is the neutral value ")