# 46) WAP to find out the sum of first and last digit of a user entered number 
n =1234
last = n%10
org = n
count = 0
while(n!=0):
    count +=1
    n=n//10
n=org
first = n//(10**(count-1))

sum = first + last
print(sum)