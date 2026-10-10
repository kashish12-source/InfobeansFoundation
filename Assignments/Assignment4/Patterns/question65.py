n=5
for i in range(1,6):
    for j in range(1,6):
        if j<i:
            print(" ",end="")
    for j in range(n-i+1):
        print("*",end="")
    print()

# *****
#  ****
#   ***
#    **
#     *