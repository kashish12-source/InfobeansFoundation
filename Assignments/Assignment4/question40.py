# 40) WAP to count no. Of even and odd digits in a number

n =1200
even = 0
odd = 0
zero=0
while(n!=0):
    dig = n%10
    if dig==0:
        zero+=1
    elif(dig%2==0):
        even+=1
    elif (dig%2!=0):
        odd+=1
    
    n=n//10

print(f"The no. of odd integers present is {odd}")
print(f"the no. of even intergers present is {even}")
