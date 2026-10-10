n = 7
for i in range(n):
    for j in range(n-2):
        if (j==0) or (i==n//2 and j<n-3) or (j==n-3 and (i>n//2 and i!=n-1) ) or (i==n-1 and j!=n-3):
            print("*",end="")
        else:
            print(" ",end="")
    print()

        
