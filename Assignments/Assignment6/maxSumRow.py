m =[[1,2,3],[4,15,6],[7,8,9]]
rs =[]
max =0 
for i in range(len(m)):
    sum =0
    result = []
    for j in range(len(m[i])):
        sum+=m[i][j]
        
        
    if max <sum:
        for j in range(len(m[i])):
            result.append(m[i][j])
        rs = result
        max =sum 


print(rs)