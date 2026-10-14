# 16. Count the frequency of each character in a string.
#     Example: "hello" -> {'h': 1, 'e': 1, 'l': 2, 'o': 1}

s = "hello"
result = {}
for key in s:
    if key in result:
        result[key]+=1
    else:
        result[key] =1
print(result)