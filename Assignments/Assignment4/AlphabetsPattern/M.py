n =int(input("Enter a no. here : "))

for i in range(1,n):
    for j in range(1,2*n):
        if j==1  or i==j or (i+j==2*n ) or j==2*n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
# *         *
# **       **
# * *     * *
# *  *   *  *
# *   * *   *