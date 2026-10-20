# 30. Find the longest common prefix among a list of strings.
# Example: ["flower", "flow", "flight"] → "fl"
l = ["flower", "flow", "flight"]

l.sort()

first = l[0]
last = l[-1]

result = ""

for i in range(min(len(first), len(last))):
    if first[i] == last[i]:
        result += first[i]
    else:
        break

print(result)