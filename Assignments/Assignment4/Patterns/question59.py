for i in range(5):
    k=65
    for j in range(5,0,-1):
        if j>i:
            print(" ",end="")
    for j in range(0,2*i+1):
        print(chr(k),end="")
        k+=1
    print()

#      A
#     ABC
#    ABCDE
#   ABCDEFG
#  ABCDEFGHI