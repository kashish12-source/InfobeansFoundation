m = [[1,2,3],[4,5,6],[7,8,9]]

max = 0
max_row = []
max_index = 0

min_row = m[0]
min = 0
min_index = 0

for j in range(len(m[0])):
    min += m[0][j]

for i in range(len(m)):
    sum = 0
    max_result = []
    min_result = []

    for j in range(len(m[i])):
        sum += m[i][j]
        max_result.append(m[i][j])
        min_result.append(m[i][j])

    if sum > max:
        max = sum
        max_row = max_result
        max_index = i

    if sum < min:
        min = sum
        min_row = min_result
        min_index = i

print(max_row)
print(min_row)

m[min_index], m[max_index] = m[max_index], m[min_index]

print(m)