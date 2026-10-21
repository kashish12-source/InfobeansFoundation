# 17. Count the frequency of each number in a list.
#     Example: [1, 2, 2, 3, 1, 2] -> {1: 2, 2: 3, 3: 1}

l = [1,2,3,2,4,2,3,53,6]
result = {}
for i in l:
    if i in result:
        result[i]+=1
    else:
        result[i]=1
print(result)
