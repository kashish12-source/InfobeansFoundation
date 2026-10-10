n = int(input("Enter a no. here : "))

for i in range(1,n):
    for j in range(1,n):
        if i==1 or i==n-1 or j==n//2:
            print("*",end="")
        else:
            print(" ",end="")
    print()
# *******
#    *   
#    *   
#    *   
#    *   
# *******