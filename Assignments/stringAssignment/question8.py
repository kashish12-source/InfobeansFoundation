# 8. Remove all spaces from a string.
s = "a for apple   "
res = ""
for i in s:
    if i != " ":
        res+=i
print(res)