# 3) WAP to find out the sum of N natural number.
i = 1
sum =0
n=int(input("enter a no. here : "))
while(n!=0):
    sum+=i
    i+=1
    n-=1
print(f"sum of n natural numbers is : {sum}")