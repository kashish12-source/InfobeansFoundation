# 7. Convert lowercase characters to uppercase without using upper().
#   s = "inDor434e"  => "INDOR434E"

def lower_to_upper(s):
    res=""
    for i in s :
        if 97<=ord(i)<=122:
            res+=chr(ord(i)-32)
        else:
            res+=i
    return res

s = "inDor434e"
print(f"The uppercase converted string is : {lower_to_upper(s)}")
