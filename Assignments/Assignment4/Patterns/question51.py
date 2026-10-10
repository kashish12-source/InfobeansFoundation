for i in range(5,0,-1):
    k=65
    for j in range(5,0,-1):
        if j>i:
            print(" ",end="")
        else:
            
            print(chr(k),end="")
            k+=1
    print()

# ABCDE
#  ABCD
#   ABC
#    AB
#     A
