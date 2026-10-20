# 26. Find the longest word in a sentence.
s ="welcome to python to world"
l = s.split()
print(l)
d ={}
for i in l :
    d[i] = len(i)
max =0 
res = ""
for i in d.keys():
    if d[i]>max:
        max = d[i]
        res = i
print(res , max)

