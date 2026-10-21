# 12. Check whether two strings are equal without using == for the complete strings.
def check_two_string(s,t):
    f = True
    
    if len(s)!=len(t):
        return False

    else:
        for i in range(len(s)):
            if ord(s[i]) != ord(t[i]):
                return False
    return True

  
s = "nitin"
t = "nitin"
if check_two_string(s,t):
    print("same")
else:
    print("Not same ")