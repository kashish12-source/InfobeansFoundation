# 14. Remove all digits from a string.
s = "abcd2353fa@ds"
res = ""
for i in s :
    if not i.isdigit():
        res+=i
print(res)