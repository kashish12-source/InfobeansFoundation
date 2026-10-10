n=7
for i in range(n):
    for j in range(n-2):
        if ((i>n//2 and i<n-1) and j==0) or (i==n//2 and j!=0) or (i==n-1 and j!=0) or (j==n-3):
            print("*",end="")
        else:
            print(" ",end="")
    print()