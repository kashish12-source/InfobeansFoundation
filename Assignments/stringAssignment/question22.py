# 22. Find the second most frequent character.
s ="abcdeabsbabbacde"
d ={}
for i in s:
    if i != " ":
        if i in d:
            d[i]+=1
        else:
            d[i]=1
d_sort = dict(sorted(d.items(),key = lambda x:x[1]))

print(d_sort)

keys = list(d_sort.keys())

print(f"The second most frequent is : {keys[-2]} : {d[keys[-2]]}")

