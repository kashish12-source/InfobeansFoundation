n= int(input("Enter a no. here :  "))
k=n-1
for i in range(1,n+1):
    for j in range(1,2*n):
        if i==j or j==2*n-i:
            print("*",end="")
        else:
            print(" ",end="")
    k-=1 
    print()

# *           *
#  *         *
#   *       *
#    *     *
#     *   *
#      * *
#       *
