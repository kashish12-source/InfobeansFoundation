# 32. Given two arrays of integers A and B of sizes M and N respectively. Write a Write a java program, which will produce a third array named C. such that the following sequence is followed. 
# All even numbers of A from left to right are copied into C from left to right. 
# All odd numbers of A from left to right are copied into C from right to left. 
# All even numbers of B from left to right are copied into C from left to right. 
# All old numbers of B from left to right are copied into C from right to left.
# e.g., A is {3, 2, 1, 7, 6, 3} and B is {9, 3, 5, 6, 2, 8, 10} the resultant array C is {2, 6, 6, 2, 8, 10, 5, 3, 9, 3, 7, 1, 3} 
a =[3, 2, 1, 7, 6, 3]
b=[9, 3, 5, 6, 2, 8, 10]
result = []
i=0

for k in a:
    if k%2==0:
        result.append(k)
        i+=1
for k in b:
    if k%2==0:
        result.append(k)
        i+=1
j=i
for k in range(len(b)-1,-1,-1):
    if b[k]%2!=0:
        result.append(b[k])
        j+=1
for k in range(len(a)-1,-1,-1):
    if a[k]%2!=0:
        result.append(a[k])
        j+=1
print(result)
