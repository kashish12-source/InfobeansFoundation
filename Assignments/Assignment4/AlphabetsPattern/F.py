n = int(input("Enter a no. greater than 5 : "))
if n>5:
    for i in range(1,n):
        for j in range(1,n-2):
            if j==1:
                print("*",end="")
            elif i==1 or i==n//2:
                print("*",end=" ")
            else:
                print(" ",end="")
        print()
else:
    print(" Enter a no. greater than 5 :")
# ** * * 
# *   
# *   
# ** * * 
# *   
# *   
# *   
