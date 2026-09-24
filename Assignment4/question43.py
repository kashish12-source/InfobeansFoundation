# 43) WAP to convert binary number into decimal number

n = 20
org = n
res = ""

while(n != 0):
    dig = n % 2
    res = str(dig) + res  
    n = n // 2

print(res) 
