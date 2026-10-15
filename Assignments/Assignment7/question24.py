# 24. Group a list of words according to their length.
#     Example: ["cat", "apple", "dog", "mango"]
#     Expected groups: 3 -> ["cat", "dog"], 5 -> ["apple", "mango"]
d = ["cat", "apple", "dog", "mango"]

result = {}

for i in d:
    if len(i) in result:
        result[len(i)].append(i)
    else:
        result[len(i)] = [i]

print(result)