for i in range(1,7):
    for j in range(1,7):
        if i==1 or j==4 or (i==6 and j<4) or (i==5 and j==1):
            print("*",end="")
        else:
            print(" ",end="")
    print()

# ******
#    *  
#    *  
#    *  
# *  *  
# ****  
