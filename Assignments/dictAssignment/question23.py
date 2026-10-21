# Sort a dictionary by its values in ascending order.
d = {'a':2,'b':3,'c':7,'d':5}

for i in d.keys():
    for j in d.keys():
        if d[i]<d[j]:
            d[i],d[j] = d[j],d[i]
print(d)
