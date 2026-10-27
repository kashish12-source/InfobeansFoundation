# 31. Find the longest substring without repeating characters.
# Example: "abcabcbb" → 3 ("abc")

s = "abcabcbb"
def longest_substring(s):
    
    left =0
    max_length = 0
    res = ""
    seen =set()
    for i in range(len(s)):
        while(s[i]) in seen:
            seen.remove(s[left])
            

            left+=1

        seen.add(s[i])
        if i - left + 1 > max_length:
            
            res = s[left:i + 1]
        max_length = max(max_length, i -left +1)
    return res,max_length

s = "abcabcbb"
res ,max_length = longest_substring(s)
print(res)
print(max_length)

