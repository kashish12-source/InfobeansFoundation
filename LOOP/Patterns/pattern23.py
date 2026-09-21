
for i in range(1,6):
    k=1
    for j in range(5,0,-1):
        if(j<=i):
            print(k,end="")
            k+=1
        else:
            print(" ",end="")
    print()