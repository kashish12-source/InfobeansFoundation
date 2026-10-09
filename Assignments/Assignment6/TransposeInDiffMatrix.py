m = [[1,2,3],[4,5,6],[7,8,9]]
result = [[0]*3,[0]*3,[0]*3]

for i in range(len(m)):
    for j in range(len(m[i])):
        result[j][i]=m[i][j]
print(result)