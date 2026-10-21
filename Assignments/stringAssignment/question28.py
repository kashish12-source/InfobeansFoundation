# 28. Check whether one string is a rotation of another.
# Example: "abcd" and "cdab" → True

s =list("abcd")
n ="cdab"
i =len(s)
while(i!=0):
        
    item = s[len(s)-1]
    for j in range(len(s)-1,0,-1):
        s[j]=s[j-1]
    s[0]= item
   
    if  "".join(s) == n:
        print("yes ")
        break
    i-=1


