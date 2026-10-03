#  Suppose A, B, C are arrays of integers of size M, N, and M + N respectively. The numbers in array A appear in ascending order while the numbers in array B appear in descending order. Write a java progtam to produce third array C by merging arrays A and B in ascending order. 
a = [1,2,4,6,8]
b =[9,7,5,3,1]
result = []
i=0
j =0
while(i<len(a) and j<len(b)):
    if (a[i]<b[j]):
        
            result.append(a[i])
            i+=1
    elif a[i]>b[j]:
       
            result.append(b[j])
            j+=1
    elif a[i] == a[j]:
       
            result.append(a[i])
            i+=1
            j+=1
while(i<len(a)):
    result.append(a[i])
    i+=1
while(j<len(b)):
    result.append(a[j])
    j+=1
print(result)