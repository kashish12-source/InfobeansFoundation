# 37) WAP to check whether entered number is palindrome or not
n =int (input("enter a no. here : "))

org = n
res =0
while(n!=0):
    dig = n%10
    res = res*10+dig
    n=n//10

n=org
if(org == res):
    print("the no. is palindrome")
else:
    print("the no. is not palindrome ")