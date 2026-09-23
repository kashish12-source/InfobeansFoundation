# 39) WAP to check whether entered number is strong or not

n = 6
org = n
res=0
for i in range(1,n//2+1):
    if(n%i == 0):
        res+=i
if(res==org):
    print("is strong")
else:
    print("Not strong")
