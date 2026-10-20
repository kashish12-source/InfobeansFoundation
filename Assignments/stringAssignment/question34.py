# 34. Compress a string by counting consecutive repeated characters.
# Example: "aaabbccccd" → "a3b2c4d1"
s = "aaabbccccd"
d ={}
for i in s :
    if i in d:
        d[i] +=1
    else:
        d[i]=1
for key,value in d.items():
    print(f"{key}{value}",end="")
