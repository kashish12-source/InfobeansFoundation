# 10. Replace every space with a hyphen (-).
def Replace_space(s):
    start = 0
    end = len(s)-1
    while(s[start] == " "):
        start +=1
    while(s[end] == " "):
        end -=1
    
    res =""
    for i in range(start , end+1) :
        if s[i] == " ":
            res+="-"
        else:
            res+=s[i]
    return res
s ="How are you "
print(Replace_space(s))
        