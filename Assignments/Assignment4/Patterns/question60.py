for i in range(1,6):
    for j in range(5,0,-1):
        if(j>i):
            print(" ",end="")
    for j in range(2*i-1):
        if j==0 or i==5 or j==2*i-2:
            print("*",end="")
        else:
            print("_",end="")
    print()

#     *
#    *_*
#   *___*
#  *_____*
# *********