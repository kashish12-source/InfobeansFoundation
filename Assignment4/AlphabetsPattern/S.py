n =int(input("Enter a no. here : "))

for i in range(1,n):
    for j in range(1,(n//2)+1):
        if (j==1 and (i>1 and i<n//2)) or (i==1 and j>1 ) or (i==n//2 and (j>1 and j<n//2 )) or (i>(n//2) and i<n-1) and j==n//2 or (i==n-1 and j<(n//2)):
            print("*",end="")
        else:
            print(" ",end="")
    print()

#  ****
# *
# *
# *
#  ***
#     *
#     *
#     *
# ****