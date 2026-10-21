# 19. Find all duplicate elements in a list and their frequencies.
l=[1,2,4,3,2,3,5,2,36,37,8,8]
result = {}
for i in l:
    if i in result:
        result[i]+=1
    else:
        result[i] =1
for i in result.keys():
    if result[i]>1:
        print(i, result[i])
