# # 16. Check whether two strings are anagrams.
# Example: "listen" and "silent" → True

s = "listAn"
t = "silent"

s_sorted = "".join(sorted(s))
t_sorted = "".join(sorted(t))

if len(s_sorted)!=len(t_sorted):
    print("The two strings are not anagram")
    
else:
    for i in range(len(s_sorted))  :
        if s_sorted[i] != t_sorted[i]:
            print("The two strings are not anagram ")
            break
    else:
        print("The two strings are anagram")
