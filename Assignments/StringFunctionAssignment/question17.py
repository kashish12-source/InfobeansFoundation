# 17. Find the first non-repeating character in a string.
# Example: "aabbcddee" → c
def non_repeating(s):
    d ={}
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for i in d.keys():
        if d[i] == 1:
            return i
    return False
s = "aabccdbefc"
if non_repeating(s):
    print(non_repeating(s))
else:
    print("No repeating alphabetsare their")