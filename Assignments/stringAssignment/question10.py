# 10. Replace every space with a hyphen (-).
s = "  a for apple b for ball "
res=""
start = 0 
end = len(s)-1
while(s[start] ==" "):
    start +=1
while(s[end] == " "):
    end-=1
while(start<end+1):
    if s[start] == " ":
        res+="-"
        start +=1
    else:
        res+=s[start]
        start+=1
print(res)