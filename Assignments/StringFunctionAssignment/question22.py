# 22. Find the second most frequent character.
def second_freq(s):
    d={}
    for i in s :
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    sorted_dict = dict(sorted(d.items(),key=lambda x:x[1]))
    key = list(sorted_dict.keys())
    return key[-2]

s = "kashishshhhdf"
res = second_freq(s)
print(f"The second most frequent character is : {res}")

