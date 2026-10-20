# 12. Check whether two strings are equal without using == for the complete strings.
s = "abcdefg"
t = "ab2defg"
if len(s)!=len(t):
    print("The two strings are not equal")
else:
    f = True
    for i in range(len(s)):
        if ord(s[i])!=ord(t[i]):
            f = False
            break
       
    if f :
        print("The two strings are same ")
    else:
        print("Two strings are not equal")
