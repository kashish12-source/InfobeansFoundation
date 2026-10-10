n=9
for i in range(n):
    for j in range(n-2):
        if j==0 or (i==0 and (j>1 and j<n-3)) or (i==n//2 and (j>1 and j<n-3)) or ((i>0 and i<n//2 )and j==1) or  ((i>0 and i<n//2 )and j==n-3):
            print("*",end="")
        else:
            print(" ",end="")
    print()