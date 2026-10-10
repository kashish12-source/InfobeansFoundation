for i in range(5):
    
    for j in range(5,0,-1):
        if i<j:
            print(" ",end="")
    for j in range(0,2*i+1):
        print("*",end="")
        
    print()

#      *
#     ***
#    *****
#   *******
#  *********