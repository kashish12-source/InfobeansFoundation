# 51) WAP to reverse all the numbers between two entered numbers

num_1 = int(input("enter 1st no. here : "))
num_2= int(input("enter 2nd no. here : "))

for i in range(num_1,num_2+1):
    temp = i
    res=0
    while(i!=0):
        dig = i%10
        res= res*10+dig
        i=i//10
    print(f"the original no. is : {temp} the reversed no. is : {res}")