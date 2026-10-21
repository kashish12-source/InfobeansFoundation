# 29. Remove a particular character from a string without using replace().
def remove_particulat_char(s,target):
    res =""
    for i in s :
        if i != target:
            res+=i
    return res

s = "abcdggggggggggdsflj"
tar = "g"
print(f"The result of the string '{s}' after removing the letter '{tar}' from it is : {remove_particulat_char(s,tar)}")

    