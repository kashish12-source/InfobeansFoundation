# 28. Check whether one string is a rotation of another.
# Example: "abcd" and "cdab" → True
def check_roatation(s,t):
    s = list(s)
    i = len(s)

    while(i!=0):
        item = s[len(s)-1]
        for j in range(len(s)-1,0,-1):
            s[j]=s[j-1]
        s[0]=item
        if "".join(s) == t:
            return True
        i-=1

s ="abcd"
t = "cdab"
if check_roatation(s,t):
    print("yes")
else:
    print("No")
    