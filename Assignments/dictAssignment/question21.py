#  Combine two dictionaries by adding the values of common keys.
#     Example: {'a': 10, 'b': 20} and {'b': 5, 'c': 7}
#     Expected: {'a': 10, 'b': 25, 'c': 7}

d1 = {'a': 10, 'b': 20}
d2 = {'b': 5, 'c': 7}


result = d1.copy()


for key, value in d2.items():
    if key in result:
        result[key] += value  
    else:
        result[key] = value   
print(result)

