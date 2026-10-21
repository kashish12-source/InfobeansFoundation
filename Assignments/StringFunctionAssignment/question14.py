# 14. Remove all digits from a string.
def Remove_digit(s):
    res =""
    for i in s :
        if not i.isdigit():
            res+=i
    return res

s = "23kfia@dalk#1"
print(Remove_digit(s))