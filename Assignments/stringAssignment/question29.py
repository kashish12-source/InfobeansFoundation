# 29. Remove a particular character from a string without using replace().
s = "kashish"
res =""
tar = "s"
for i in s :
    if i!=tar:
        res+=i
print(res)