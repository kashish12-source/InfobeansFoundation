k=65
for i in range(1,6):
    for j in range(5,0,-1):
        if i<j:
            print(" ",end="")
    for j in range(1,2*i):
        if j==1 or j==2*i-1 or i==5:
            print(chr(k),end="")
        else:
            print(" ",end="")
    print()
    k+=1
#     A
#    B B
#   C   C
#  D     D
# EEEEEEEEE