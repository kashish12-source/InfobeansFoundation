# 42) WAP to find out LCM of a number

n1 = 4
n2 = 6
result=1
for i in range(1,n2*n1+1):
    if i%n1 == 0 and i%n2 == 0:
        result =i
        break
print(result)