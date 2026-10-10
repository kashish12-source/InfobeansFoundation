n= int(input("Enter a no. here : "))
for i in range(1,n):
    for j in range(1,n//2+1):
        if (i==1 and j!=n//2) or j==1 or (i==n//2 and j!=n//2) or (j==n//2 and (i<n//2 and i!=1)):
            print("*",end="")
        else:
            print(" ",end="")
    print()

# ***
# *  *
# *  *
# ***
# *
# *
# *