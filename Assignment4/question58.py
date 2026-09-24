# 58) WAP to convert decimal number into binary number without using array

# n = int(input("Enter the decimal no. here : "))
n=10
org =n 
res =""
while(n!=0):
    dig = n%2
    res = str(dig)+res
    n=n//2
print(res)