m =[[1,2,3],[4,15,6],[7,8,9]]
n=[[1,2,3],[4,15,6],[7,8,9]]

result = []

for i in range(len(m)):
    row = []

    for j in range(len(n[0])):
        sum = 0

        for k in range(len(n)):
            sum += m[i][k] * n[k][j]

        row.append(sum)

    result.append(row)

print(result)