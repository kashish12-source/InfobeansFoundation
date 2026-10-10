n=int(input("Enter no. here : "))

for i in range(1,n):
    for j in range(n-1,0,-1):
        if i==1 or i==n-1 or i==j:
            print("*",end="")
        else:
            print(" ",end="")
    print()
# ******
#     *
#    *
#   *
#  *
# ******