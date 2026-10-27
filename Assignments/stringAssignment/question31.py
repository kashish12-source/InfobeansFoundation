# 31. Find the longest substring without repeating characters.
# Example: "abcabcbb" → 3 ("abc")

s = "abcabcbb"
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

print(max_length)
print(res)

