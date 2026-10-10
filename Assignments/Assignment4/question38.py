# 38) WAP to check whether entered number is Armstrong or not

# n= int(input("Enter a no.  here : "))
n=153
org = n
count = 0
while(n!=0):
    count+=1
    n=n//10
n=org
res=0
while(n!=0):
    dig = n%10
    res+=dig**count
    n=n//10
if(org == res):
    print("The no. is armstrong")
else:
    print("The no. is not armstrong")