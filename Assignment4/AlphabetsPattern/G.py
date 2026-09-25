for i in range(1,7):
    for j in range(1,6):
        if i==1 or j==1 or i==6:
            print("*",end="")
        else:
            print(" ",end="")
    for j in range(5,8):
        if i == 4  or j==7 and i>=4:
            print("*",end="")
        elif i==j and j!=6:
            print("*",end="")

        else:
            print(" ",end="")
    print()
# *****   
# *       
# *       
# *    ***
# *    * *
# *****  *