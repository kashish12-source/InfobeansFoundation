# 29. Given two dictionaries, return the keys whose values are equal in both.
d1 = {
    "a": 10,
    "b": 20,
    "c": 30,
    "d": 40
}

d2 = {
    "a": 10,
    "b": 50,
    "c": 30,
    "e": 60
}
result={}
for i in d1.keys():
    if i in d2:
        if d1[i] == d2[i]:
            result[i]= d1[i]
print(result.keys())
