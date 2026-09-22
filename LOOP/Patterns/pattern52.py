for i in range(1,6):
    k=65
    for j in range(5,0,-1):
        if(j<=i):
            print(chr(k),end="")
            k+=1
        else:
            print(" ", end="")
    print()
#     A
#    AB
#   ABC
#  ABCD
# ABCDE