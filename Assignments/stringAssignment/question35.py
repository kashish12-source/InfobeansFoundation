# 35. Expand a compressed string.
# Example: "a3b2c4" → "aaabbcccc"
s = "a3bb2c4"
word = ""
res = ""

for i in s:
    if i.isalpha():
        word += i
    else:
        res += word * int(i)
        word = ""

print(res)