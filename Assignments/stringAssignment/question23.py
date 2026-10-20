# 23. Reverse the order of words in a sentence.
# Example: "Python is easy" → "easy is Python"

s ="Python is easy"
l = s.split()

print(l)

res=""
for i in range(len(l)-1,-1,-1):
    res+=l[i]
    if i>0:
        res+=" "
print(res)