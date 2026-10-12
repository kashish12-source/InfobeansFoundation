l = ["any","and","if"]
result = {len(element) : [] for element in l}
for x in l:
    result[len(x)].append(x)
# l = ["any", "and", "if"]

# result = {
#     length: [x for x in l if len(x) == length]
#     for length in {len(x) for x in l}
# }


print(result)