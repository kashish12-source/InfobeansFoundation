m =[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(m)):
    for j in range(len(m[i])):
        start = 0
        end = len(m[i])-1
        while(start<end):
            m[i][start],m[i][end]= m[i][end],m[i][start]
            start +=1
            end -= 1
print(m)