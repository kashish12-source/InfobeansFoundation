# 9. Find the first and last character of a string.
s = "abcdefghijklmnopqrst    "
start = 0
end = len(s)-1
while(s[start] == " "):
    start+=1
while(s[end] ==" "):
    end-=1
print(f"The first character of a string is : {s[start]}")
print(f"The last character of a string is : {s[end]}")
