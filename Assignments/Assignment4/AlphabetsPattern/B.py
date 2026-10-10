n = int (input("Enter the input here : "))

for i in range(1,n):
    for j in range(1,n):
        if (j==1 ) or (i==1 and j<n-1) or (i==n//2 and j<n-1) or (i==n-1 and j<n-1) or (j==n-1 and (i!=1 and i!=n//2)) and (j==n-1 and (i!=n//2 and i!=n-1)):
            print("*",end="")
        else:
            print(" ",end="")
    print()
# ******
# *     *
# *     *
# ******
# *     *
# *     *
# ******