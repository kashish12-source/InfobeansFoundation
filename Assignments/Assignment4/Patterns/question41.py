for i in range(5,0,-1):
    for j in range(1,i):
        print(" ",end="")
    for j in range(1,6):
        if j>=i and j<=5:
            print(i,end="")
    print()
#     5
#    44
#   333
#  2222
# 11111
