# 27. Find all duplicate characters and their frequencies.
def duplicate_charcters(s):
    d ={}
    for i in s:
        if i in d :
            d[i]+=1
        else:
            d[i]=1
    res={}
    for i in d.keys():
        if d[i]>=2:
            res[i] = d[i]
    return res
s ='abcdaansdbfaadjiojdjl'
result = duplicate_charcters(s)
print(result)