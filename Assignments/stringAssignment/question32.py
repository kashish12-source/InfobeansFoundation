# 32. Find the longest palindromic substring.
# Example: "babad" → "bab" or "aba"

s = "babad"
res = ""

for i in range(len(s)):
    # Odd-length palindrome
    left = i
    right = i

    while left >= 0 and right < len(s) and s[left] == s[right]:
        if right - left + 1 > len(res):
            res = s[left:right + 1]

        left -= 1
        right += 1

    # Even-length palindrome
    left = i
    right = i + 1

    while left >= 0 and right < len(s) and s[left] == s[right]:
        if right - left + 1 > len(res):
            res = s[left:right + 1]

        left -= 1
        right += 1

print(res)
