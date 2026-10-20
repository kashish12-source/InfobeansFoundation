# 24. Reverse every word without changing the word order.
# Example: 24. Reverse every word without changing the word order.
# Example: "Python is easy" → "nohtyP si ysae" → "nohtyP si ysae"

s = "Python is easy"

words = s.split()
res = []
print(words)
for word in words:
    res.append(word[::-1])

print(res)
print(" ".join(res))