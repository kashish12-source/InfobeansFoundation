#  Group words that are anagrams of one another.
#     Example: ["eat", "tea", "bat", "ate"]
#     Expected groups: ["eat", "tea", "ate"] and ["bat"]



result = {}
l = ["eat", "tea", "bat", "ate"]

for word in l:
    key = "".join(sorted(word))

    if key not in result:
        result[key] = []

    result[key].append(word)

print(list(result.values()))
