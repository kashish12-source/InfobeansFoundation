# 13) WAP to print N natural numbers in reverse order

n = int (input("Enter a no. here : "))

org =n
res = 0
while(n!=0):
    dig = n%10
    res= res*10+dig
    n =n //10
print(res)