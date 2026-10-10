for i in range(5,0,-1):
    for j in range(5,0,-1):
        if(j>i):
            print(" ",end="")
        else:
            if(i==j) or i == 5 or j==1:
                print(i,end="")
            else:
                print("_",end="")   

    print()

# 55555
#  4__4
#   3_3
#    22
#     1