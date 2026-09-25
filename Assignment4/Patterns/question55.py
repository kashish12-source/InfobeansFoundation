for i in range(5,0,-1):
    k =65
    for j in range(1,6):
        if(i>j):
            print(" ",end="")
        else:
            print(chr(k),end=" ")
            k+=1
    print()
#     A 
#    A B 
#   A B C 
#  A B C D 
# A B C D E 
