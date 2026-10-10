for i in range(5,0,-1):
    for j in range(1,6):
        if(j<i):
            print(" ",end="")
        else:
            if i==j or j == 5 or i==1:
                print("x",end="")
            else:
                print("_",end="")
    print()
#     x
#    xx
#   x_x
#  x__x
# xxxxx
