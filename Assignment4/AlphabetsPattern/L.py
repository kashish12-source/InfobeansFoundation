n= int(input("Enter a no. here : "))
for i in range(1,n):
    for j in range(1,n):
        if j ==1 or i==n-1 and j<=n//2+2:
            print("*",end="")
    print()
# *
# *
# *
# *
# *
# *
# *****