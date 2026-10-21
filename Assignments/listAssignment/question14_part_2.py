arr = [1,2,3,4,2,3,4,6,7,8,6]
s = set()
result = None
for i in arr[::-1]:
    if arr[i] in s:
        result = arr[i]
    s.add(arr[i])
print(result)