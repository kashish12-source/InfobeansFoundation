# 18. Find the first repeating character.
# Example: "programming" → r

s="programming"
d={}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for i in d.keys():
    if d[i]==2:
        print(f"The first repeating element is : {i}")
        break
else:
    print("All the elements in the string is repetative ")
    