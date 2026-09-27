for i in range(1,9):
    if i<=4:
        for j in range(5,0,-1):
            if j==5:
                print("*",end="")
            if i<j:
                print(" ",end="")
            elif i==j :
                print("*",end="")
        print()
    else:
        for j in range(3,9):
            if j==3 or i==j:
                print("*",end="")
            
            else:
                print(" ",end="")
        print()

# *    *
# *   *
# *  *
# * *
# * *   
# *  *  
# *   * 
# *    *
