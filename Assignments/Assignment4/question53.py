# 53) WAP to print all the strong numbers between two entered numbers
num_1 = int(input("enter the first no. here : "))
num_2 =int(input("enter the second no. here : "))
for i in range(num_1 , num_2+1):
    res = 0
    for j in range(1,(i//2)+1):
        if(i%j==0):
            res+=j
        
    if(res==i):
        print(f"The strong no. is {res}")