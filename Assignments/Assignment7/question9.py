# Find the key associated with the largest value in a dictionary.
students = {"a":42,
            "b":92,
            "c":45,
            "d":75}

max = 0
result = ""
for value in students.keys():
    k=students[value]
    if k > max:
        max = k
        result = value 

print(f"the key with the maximum value is : {result} = {max}")