# 18. Find the first repeating character.
# Example: "programming" → r
def Repeating(s):
    d = {}
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for i in d.keys():
        if d[i]>=2:
            return i
    return False

s = "abcdef"
if Repeating(s):
    print(f"The first repeating element is : {Repeating(s)}")
else:
    print("All the elements are singly occured ")