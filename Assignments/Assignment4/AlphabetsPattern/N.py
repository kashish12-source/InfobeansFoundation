n = int(input("Enter no. here : "))
for i in range(1,n):
    for j in range(1,n):
        if j==1 or i==j or j==n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
# *   *
# **  *
# * * *
# *  **
# *   *