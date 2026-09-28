n = int(input("enter the number here : "))
if(n<1000 and n>9999):
    print("please enter a four digit number ")
else:
    d4 = n%10
    n = n//10
    
    d3 =n%10
    n = n//10
    
    d2 = n%10
    n = n//10   
    
    d1 = n%10   
    
    print(f"the reversed number is : {d4*1000 + d3*100 + d2*10 + d1}")
