n = 5 
for i in range(1,6):
    for j in range(0,n-i):
        print(" ",end="")
    for j in range(1,2*i):
        print("*",end="")
    print()

#     *
#    ***
#   *****
#  *******
# *********