# 30) 1+11+111+1111+11111. 
n = int(input("Enter a no. here : "))
i =0
while(n!=0):
    for j in range(0,i):
        print("1",end="")
    print("+",end="")
    i+=1
    n-=1
for  j in range(0,i):
    print("1",end="")
