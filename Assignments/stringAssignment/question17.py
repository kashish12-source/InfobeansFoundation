# 17. Find the first non-repeating character in a string.
# Example: "aabbcddee" → c

s ="aabbccdee"
d ={}
for i in s :
    if i in d:
        d[i] +=1
    else:
        d[i]=1
for i in d.keys():
    if d[i]==1:
        print(i)
        break
else:
    print("There is no non-repeating character in the string ")
    
