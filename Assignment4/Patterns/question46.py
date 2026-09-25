for i in range(5):
    k=1
    for j in range(1,6):
        if(j<=i):
            print(" ",end="")
        else:
            print(k,end="")
            k+=1
    print()

# 12345
#  1234
#   123
#    12
#     1