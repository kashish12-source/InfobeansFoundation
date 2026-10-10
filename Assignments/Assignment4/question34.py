# 34) WAP to check whether entered number is perfect or not
n= int(input("Enter a no. here : "))
result=0
for i in range(1,n//2+1):
    if(n%i==0):
        result+=i
if(result==n):
    print("it is a perfect no. ")
else:
    print("it is not a perfect no.")