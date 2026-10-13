# 11. Create a dictionary from two lists: one list contains keys and the
#     other contains values. Do not use zip().

d = {"k":["hii",2,3,4,5],"v":['kashish',"keshav","raghav","kartavya","koshiki"]}
result = {}
key_list = d["k"]
value_list = d['v']
for i in range(len(key_list)):
    key = key_list[i]
    value = value_list[i]
    result[key] = value
print(result)