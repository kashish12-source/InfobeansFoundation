for i in range(5,0,-1):
    k=1
    for j in range(5,0,-1):
        if(j>i):
            print(" ",end="")
        else:
            if i==j or j==1 or i==5:
                print(k,end="")
                k+=1
            else:
                print(" ",end="")
                k+=1
    print()
# 12345
#  1  4
#   1 3
#    12
#     1