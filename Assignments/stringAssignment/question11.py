# 11. Count how many times a particular character occurs.
s = "abcdefabcabcaddbeedf"
target = "k"
d = {}
for i in s :
    if i in d:
        d[i]+=1
    else:
        d[i] = 1
res=0
for i in d.keys():
    if i == target:
        res = d[i]
        
        
if res:
    print(f"The no. of times the charcter occur is : {res}")
else:
    print(f"The character is not present in the string")

