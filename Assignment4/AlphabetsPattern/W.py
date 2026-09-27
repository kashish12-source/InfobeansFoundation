n= int(input("Enter a no. here : "))

for i in range(n,0,-1):
    for j in range(1,2*n):
        if (i==j) or (j==1) or (j>n and i+j==2*n) or j==2*n-1 :
            print("*",end="")
        else:
            print(" ",end="")
    print()
# *      *      *
# *     * *     *
# *    *   *    *
# *   *     *   *
# *  *       *  *
# * *         * *
# **           **
# *             *