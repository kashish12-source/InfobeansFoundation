# 1. Write a program to reverse a string without using slicing ([::-1]).
def reverse_string(s):
    res = ""
    for i in range(len(s)-1,-1,-1):
        res+=s[i]
    return res
s = "hello"
result= reverse_string(s)
print(result)