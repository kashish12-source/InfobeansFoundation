for i in range(1,8):
    if(i<=4):
        for j in range(1,i+1):
            if j==1 or i==j:
                print(j,end="")
            else:
                print(" ",end="")
        print()
    else:
        for j in range(1,8-i+1):
            if j==1 or j==8-i:
                print(j,end="")
            else:
                print(" ",end="")
        print()

# 1
# 12
# 1 3
# 1  4
# 1 3
# 12
# 1