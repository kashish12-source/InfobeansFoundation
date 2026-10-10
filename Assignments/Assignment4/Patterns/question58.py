for i in range(5):
    k=1
    for j in range(5,0,-1):
        if j>i:
            print(" ",end="")
    for j in range(0,2*i+1):
        print(k,end="")
        k+=1
    print()
#      1
#     123
#    12345
#   1234567
#  123456789