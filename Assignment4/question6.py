# 6) WAP to find out the factors of a number.

n = int (input("Enter a no. here : "))
for i in range(1,n//2+1):
    if(n%i==0):
        print(i)
print(n)