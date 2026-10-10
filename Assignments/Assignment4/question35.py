# 35) WAP to count number of digits
n = int(input("Enter a no. here : "))
count = 0
while(n!=0):
    
    count = count+1
    n=n//10

print(count)