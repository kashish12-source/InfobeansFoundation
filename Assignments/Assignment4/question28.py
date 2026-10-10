# 28) 1	2	3	4	 Hello	6	7	8	9	Hello	11	12 ….
n = int(input("enter a no. here : "))
i=1
while(n!=0):
    if(i%5==0):
        print(" hello ",end=" ")
    else:
        print(i,end=" ")
    i+=1
    n-=1
    