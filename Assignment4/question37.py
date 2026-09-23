# 36) WAP to reverse a number

n = int(input("Enter a no. here : "))
result= 0
while(n!=0):
    dig  = n%10
    result = result*10+dig
    n = n//10

print(result)