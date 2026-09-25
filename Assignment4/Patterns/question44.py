for i in range(1,6):
    k = 65
    for j in range(5,0,-1):
        if i==5 or j ==1 or i==j:
            print(chr(k),end="")
            k+=1
        else:
            if i<j:
                print(" ",end="")
            else:
                print("_",end="")
                k+=1
    print()

#     A
#    AB
#   A_C
#  A__D
# ABCDE