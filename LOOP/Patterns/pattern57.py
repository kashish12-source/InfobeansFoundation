n =5 
for i in range(1,6):
    for j in range(1,n-i+1):
        print(" ",end="")
    for k in range(1,2*i):
        if k==1 or k == 2*i-1 or i==n:
            print(1,end="")
        else:
            print("_",end="")
    print()
#     1
#    1_1
#   1___1
#  1_____1
# 111111111
