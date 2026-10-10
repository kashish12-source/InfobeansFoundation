for i in range(1,8):
    if(i<=4):
        for j in range(4,0,-1):
            if (j>i):
                print(" ",end="")
        for j in range(2*i-1):
            if j==0 or j==(2*i)-2:
                print("*",end="")
            else:
                print("_",end="")
        print()
    else:

        for j in range(1,i-3):
            print(" ",end="")
        for j in range(2*(8-i)-1):
            if j==0 or j==2*(8-i)-2:
                print("*",end="")
            else:
                print("_",end="")
        print()

#    *
#   *_*
#  *___*
# *_____*
#  *___*
#   *_*
#    *
