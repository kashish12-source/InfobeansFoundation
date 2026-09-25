
for i in range(5,0,-1):
    k =65
    for j in range(5,0,-1):
        if(j>i):
            print(" ",end="")
        else:
            if i == j or j==1 or i==5:
                print(chr(k),end="")
                k+=1
            else:
                print(" ",end="")
                k+=1
    print()

# ABCDE
#  A  D
#   A C
#    AB
#     A
