# 20. Remove duplicate characters while preserving their original order.
# Example: "programming" → "progamin"

s = "program   ming  "
d = {}
for i in s :
    if i!=" ":
        if i in d:
            d[i]+=1
        else:
            d[i]=1

res=""

for i in d.keys():
    res+=i

print(res)