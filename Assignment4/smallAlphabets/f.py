n=8
for i in range(n):
    for j in range(n):
        if (i==(n//2) and j<=n//2) or (j==n//4 and i!=0) or (i==0 and (j>=n//2 and j<n-1)) or (j==n-1 and (i!=0 and i<=n//4)):
            print("*",end="")
        else:
            print(" ",end="")
    print()