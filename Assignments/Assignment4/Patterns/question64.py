
for i in range(5,0,-1):
    for j in range(5,0,-1):
        if j>i:
            print(" ",end="")
    for j in range(2*i-1):
        print("*",end="")
    print()
# *********
#  *******
#   *****
#    ***
#     *