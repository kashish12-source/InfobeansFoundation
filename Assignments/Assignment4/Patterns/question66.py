for i in range(5,0,-1):
    for j in range(5,0,-1):
        if j>i:
            print(" ",end="")
    for j in range(1,2*i):
        print(j,end="")
    print()

# 123456789
#  1234567
#   12345
#    123
#     1
