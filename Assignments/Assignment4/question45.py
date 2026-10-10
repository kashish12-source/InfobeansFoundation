# 45) WAP to find out the sum of all the digits of a number

n =1234
org= n
sum = 0
while(n!=0):
    dig = n%10
    sum+=dig
    n=n//10
print(f"sum of all the digits of the no. {org} is : {sum}")