# 41) WAP to find out HCF of a number


a =15
b=25
greatest=0
if(a>=b):
    greatest=a
else :
    greatest =b 
result =1
for i in range(2,(greatest//2)+1):
    if(a%i==0) and b%i==0:
        result=i
        
print(result)