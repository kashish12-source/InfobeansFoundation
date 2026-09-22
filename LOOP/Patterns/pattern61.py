n=5
for i in range(1,6):
    for j in range(0,n-i):
        print(" ",end="")
    for j in range(i,1,-1):
        print(j,end="")
    for j in range(1,i+1):
        print(j,end="")
    print()
#     1
#    212
#   32123
#  4321234
# 543212345
