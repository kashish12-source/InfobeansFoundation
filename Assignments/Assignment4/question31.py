# 31) 9	99	999	9999	  99999 

n = int(input("enter a no. here : "))
i=0
while(n!=0):
    for j in range(0,i):
        print(9,end="")
    print(end=" ")
    i+=1
    n-=1
for i in range(0,i):
    print(9,end="")