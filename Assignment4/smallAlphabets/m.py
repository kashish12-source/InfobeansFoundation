n=5
for i in range(n):
    for j in range(2*n):
        if j==0 or (j==(2*n)//2  and i!=0) or (i==1 and j==1 ) or (i==0 and (j>1 and j<(2*n)//2)) or (i==0 and (j>(2*n)//2 and j<2*n-1)) or (j==(2*n)-1 and i!=0):
            print("*",end="")
        else:
            print(" ",end ="")
    print()