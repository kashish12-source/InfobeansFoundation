
n= int(input("Enter a no. here : "))
for i in range(1,n):
    for j in range(1,n):
        if ((i>1 and i<n-1) and j==1) or (i==1 and j>1) or (i==n-1 and j!=1):
            print("*",end="")
        else:
            print(" ",end="")
    print()

#  ****
# *
# *
# *
#  ****