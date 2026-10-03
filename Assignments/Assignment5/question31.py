# 31. Suppose X. Y, Z are arrays of integers of size M, N, and M + N respectively. The numbers in array X and Y appear in descending order. Write a java program to produce third array Z by merging arrays X and Y in descending order. 

a = [8,6,4,3,2]
b =[90,67,4,2,1]
result = []
i=0
j =0
while(i<len(a) and j<len(b)):
    if a[i]>b[j]:
        result.append(a[i])
        i+=1
    elif b[j]>a[i]:
        result.append(b[j])
        j+=1
    elif a[i]==b[j]:
        result.append(a[i])
        i+=1
        j+=1

while(i<len(a)):
    result.append(a[i])
    i+=1
while(j<len(b)):
    result.append(b[j])
    j+=1
print(result)