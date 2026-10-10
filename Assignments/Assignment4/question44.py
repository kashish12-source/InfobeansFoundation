# 44) WAP to interchange first and last digit of a number

n =1234
last =n%10

org =n
count =0
while(n!=0):
    count+=1
    n=n//10
n= org
first = n//(10**(count-1))
middle = n%(10**(count-1))
middle = middle // 10

res = last *( 10**(count-1))+middle *10 +first
print(res)

