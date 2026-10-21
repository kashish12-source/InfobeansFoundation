# 11. Count how many times a particular character occurs.

def counting (s,tar):
    count = 0
    for  i in s :
        if i==tar:
            count+=1
    return count 

s ="abdafdiuaahiua"
tar ="a"
print(counting(s,tar))