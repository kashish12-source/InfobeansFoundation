n=8

for i in range(n):
    for j in range(n+2):
        if (j==0 and (i!=0 and i!=n-1)) or (j==n-1  and (i!=0 and i!=n-1)) or (i==0 and (j!=0 and j<n-1)) or (i==n-1 and (j!=0 and j<n-1)) or (j==n and i==0) or (i==n-1 and j>=n):
            print("*",end="")
        else:
            print(" ",end="")
    print()