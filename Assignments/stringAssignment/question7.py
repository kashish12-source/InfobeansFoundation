# 7. Convert lowercase characters to uppercase without using upper().
s = "abcdefghHIGH"
res=""
for i in s :
    if ord(i)<=122 and ord(i)>=97:
        res+=chr(ord(i)-32)
    else:
        res+=i
print(res)
