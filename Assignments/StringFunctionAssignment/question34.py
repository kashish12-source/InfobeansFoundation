# 35. Expand a compressed string.
# Example: "a3b2c4" → "aaabbcccc"
def counting_consicutive(s):
    word =""
    res=""
    for i in s:
        if i.isalpha():
            word+=i
        else:
            for i in range(int(i)):
                res+=word

            word=""
    return res

s = "a3b2c4d1"

print(f"The result of the string '{s}' is :{counting_consicutive(s)}")