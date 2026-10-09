m =[[1,2,3],[4,15,6],[7,8,9]]
n=[[1,2,3],[4,15,6],[7,8,9]]

result = [[0]*3,[0]*3,[0]*3]

for i in range(len(m)):
    for k in range(len(n[0])):
        for j in range(len(m[i])):
            result[i][k] += m[i][j] * n[j][k]
print(result)
