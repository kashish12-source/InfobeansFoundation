# 10. Merge two dictionaries. If a key exists in both dictionaries, use the
#     value from the second dictionary.

d1 = {
    "1":23,
    "2":35,
    "3":45
}
d2 = {
    "1":45,
    "4":42,"2":34,"6":342
}
result = {}
for k in d1.keys():
    for val in d2.keys():
        if k == val:
            result[k] = d2[val]
print(result)