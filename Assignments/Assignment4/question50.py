# 50) WAP to find out all the palindrome numbers between two entered numbers

num_1 = int(input("Enter a 1st no. here : "))

num_2 =int(input("Enter a 2nd no. here : "))

for i in range(num_1,num_2+1):
    temp = i
    res=0
    while(i!=0):
        dig = i%10
        res = res*10+dig
        i = i//10
    if(temp == res):
        print(res,end=" ")
