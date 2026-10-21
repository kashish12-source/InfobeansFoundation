# 34. Compress a string by counting consecutive repeated characters.
# Example: "aaabbccccd" → "a3b2c4d1"

def counting_cons(s):
    d ={}
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    res = ""
    for i in d.keys():
        res+=i
        res+=str(d[i])
    return res

s = "abbbcsssddd"
print(counting_cons(s))
