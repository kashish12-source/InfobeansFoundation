# 8) WAP to print Fibonacci series.
n= int (input("enter a no. here : "))

a = 0
b = 1

print(a,end=" ")
print(b,end=" ")
while(n!=0):
    k=a+b
    print(k,end=" ")
    a=b
    b=k
    n-=1

