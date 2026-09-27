n = int(input("Enter a no. here : "))


for i in range(1,n):
    for j in range(1,n-2):
        if (i==1 and j<n-3) or (j==1) or (i==n//2 and j<n-3) or j==n-3 and(i!=1 and i<n//2 ) or( i>n//2 and(i-j==2)):
            print("*",end="")

        else:
            print(" ",end="")
    print()

# ********
# *       *
# *       *
# *       *
# *       *
# ********
# *   *
# *    *
# *     *
# *      *
# *       *