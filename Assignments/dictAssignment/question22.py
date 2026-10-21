# 22. Find the common keys between two dictionaries.
d1 = {'a': 10, 'b': 20}
d2 = {'b': 5, 'c': 7,'a':34}


result = []


for key in d1.keys():
    for k in d2.keys():
        if key == k:
            result.append(k)
     
print(result)