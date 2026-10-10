# 7) WAP to check whether entered number is prime or not.

n = int (input("enter a no. here : "))
f = True
if n>1:
    for i in range(2,n//2+1):
        if(n%i==0):
            f= False
            break
else:
    f= False
if(f):
    print(f"{n} is a prime no. ")
else:
    print(f"{n} is a not prime no. ")