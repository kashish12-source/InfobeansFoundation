for i in range(1,8):
    if (i<=4):
        for j in range(4,0,-1):
            if(j>i):
                print(" ",end="")
        
        for j in range(1,2*i):
            if (j%2!=0):
                print("*",end="")
            else:
                print("_",end="")
        print()
    else:
        for j in range(5,9):
            if i==j or i>j:
                print(" ",end="")
        for j in range(1,2*(8-i)):
            if(j%2!=0):
                print("*",end="")
            else:
                print("_",end="")
        print()
#   *
#   *_*
#  *_*_*
# *_*_*_*
#  *_*_*
#   *_*
#    *