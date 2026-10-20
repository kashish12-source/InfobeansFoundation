# 27. Find all duplicate characters and their frequencies.
s = "abcdaadeaddagdfgesss"
d ={}
for i in s :
    if i!=" ":
        if i in d:
            d[i]+=1
        else:
            d[i]=1
for i in d.keys():
    if d[i]>1:
        print(f"The duplicate character is : {i} and its frequency is : {d[i]}")
        