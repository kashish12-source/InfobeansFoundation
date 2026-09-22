n = 5
for i in range(1,6):
    for j in range(1,n-i+1):
        print(" ",end="")
    for k in range(1,2*i):
        if k == 1 or k == 2*i-1 or i ==n:
            print("*",end="")
        else:
            print("_",end="")
    print()

#     *
#    *_*
#   *___*
#  *_____*
# *********