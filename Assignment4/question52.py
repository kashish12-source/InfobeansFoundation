# 52) WAP to find out all the Armstrong numbers between two entered numbers
num_1 = int(input("Enter the first no. here : "))
num_2 =int(input("Enter the second no. here : "))
for i in range(num_1 , num_2+1):
    res=0
    n=i
    temp =i
    count=0
    while(i!=0):
        count+=1
        i= i//10
    while(n!=0):
        dig = n%10
        res += dig**count
        n=n//10
    if(temp == res):
        print(f"the no. is armstrong {res}")
    