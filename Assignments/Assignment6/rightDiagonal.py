m =[[1,2,3],[4,5,6],[7,8,9]]

x = len(m)
for i in range(len(m)):
    for j in range(len(m[i])):
        if i+j ==x-1:
            print(m[i][j],end=" ")
        else:
            print("0",end=" ")
    print()