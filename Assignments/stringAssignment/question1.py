# 1. Write a program to reverse a string without using slicing ([::-1]).
s = "kashish"
res=""
for i in range(len(s)-1 , -1 , -1):
    res+=s[i]
print(res)