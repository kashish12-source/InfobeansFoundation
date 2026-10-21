# 16. Check whether two strings are anagrams.
# Example: "listen" and "silent" → True
def anagram(s,t):
    s = sorted(s)
    t = sorted(t)
    s = "".join(s)
    t = "".join(t)
    s = s.lower()
    t = t.lower()
    if len(s)!=len(t):
        return False
    else:
        for i in range(len(s)):
            if ord(s[i]) != ord(t[i]):
                return False
        return True
s ="liaten"
t = "silent"
if anagram(s,t):
    print("Is anagram")
else:
    print("Not anagram")