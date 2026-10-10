n=11
for i in range(n):
    for j in range(n//2):
        if(j==(n//2)-1) or ((i==0 and j>0)) or (i==(n//2)-1 and j>0) or (i==n-1 and j>0) or(j==0 and (i>0 and i<n//2) )or (j==0 and (i<n-1 and i>(n//2)+1)):

            print("*",end="")
        else:
            print(" ",end="")
    print()