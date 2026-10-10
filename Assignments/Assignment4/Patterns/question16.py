for i in range(1,6):
    k=1
    for j in range(1,i+1):
        if i==5 or j ==1 or i==j:
            print(k,end="")
            k+=1
        else:
            print(" ",end="")
            k+=1
    print()
# 1
# 12
# 1 3
# 1  4
# 12345