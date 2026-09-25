for i in range(1,8):
    if i<=4:
        k=1
        for j in range(4,0,-1):
            if(i<j):
                print(" ",end="")
            else:
                
                print(k,end="")
                k+=1
        print()
    else:
        k=1
        for j in range(1,5):
            if j<i-3:
                print(" ",end="")
            else:
                print(k,end="")
                k+=1
        print()

#    1
#   12
#  123
# 1234
#  123
#   12
#    1