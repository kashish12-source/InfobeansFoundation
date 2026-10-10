for i in range(1,6):
    for j in range(5,0,-1):
        if j>i:
            print(" ",end="")
    for j in range(1,2*i):
        if i%2==0:
            if (i+j)%2==0:
                print(0,end="")
            else:
                print(1,end="")
        else:
            if (i+j)%2==0:
                print(1,end="")
            else:
                print(0,end="")
    print()
#     1
#    101
#   10101
#  1010101
# 101010101