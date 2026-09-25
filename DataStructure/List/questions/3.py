l=[1,2,3,4,4,3,4,4,2,6,2,65]
target =4
res =[]
for i in range(len(l)):
    if l[i]==target:
        res.append(i)
if res:
    s="element found at : "
    for i in res:
        print(s+(str(i)))
else:
    print("element not found")