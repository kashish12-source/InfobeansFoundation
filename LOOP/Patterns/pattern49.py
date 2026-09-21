for i in range(1,6):
    for j in range(5,0,-1):
        if (i==5 or j==1 or i==j):
            print("1",end="")
        else:
            if(i<j):
                print(" ",end = "")
            else:
                print("*",end="")
    print()
#     1
#    11
#   1*1
#  1**1
# 11111