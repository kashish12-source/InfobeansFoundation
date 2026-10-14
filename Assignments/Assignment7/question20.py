# 20. Reverse a dictionary so that values become keys and keys become values.
#     Assume all values are unique.
d = {1:"hii",2:'hello',}
result={}

for key , value in d.items():
    result[value]= key
print(result)
