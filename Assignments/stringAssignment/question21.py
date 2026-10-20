# 21. Find the most frequent character in a string.
s ="nitinnnnnn"
d ={}
for i in s:
    if i!=" ":
        if i in d:
            d[i]+=1
        else:
            d[i]=1

max =0
res = ""
for i in d.keys():
    if d[i]>max:
        max = d[i]
        res=i

print(res)