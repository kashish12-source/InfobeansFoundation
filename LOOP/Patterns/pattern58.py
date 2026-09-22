n =5 
for i in range(1,6):
    for j in range(1,n-i+1):
        print(" ",end="")
    for k in range(1,2*i):
        if k == 5 or k==1:
            print("#",end="")
        else:
            print("*",end="")
    print()