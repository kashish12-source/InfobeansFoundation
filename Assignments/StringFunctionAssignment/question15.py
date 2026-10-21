# 15. Find the ASCII/Unicode value of each character using ord().
def PrintASCII(s):
    d = {}
    for i in s :
        d[i] = ord(i)
    return d

s ="abdacd"
d = PrintASCII(s)
for i in d.keys():
    print(f"{i} : {d[i]}")
    