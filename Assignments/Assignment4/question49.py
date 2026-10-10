# 49) WAP to find out all the perfect numbers between two entered numbers

num_1 = 5
num_2 =30

for i in range(num_1,num_2+1):
    res=0
    for j in range(1,(i//2)+1):
        if(i%j==0):
            res+=j
    if(res==i):
        print(res,end="  ")
    
