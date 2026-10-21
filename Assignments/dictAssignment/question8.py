# 8. Calculate the sum of all numeric values in a dictionary.

students = {"a":"kashish",
            "b":45,
            "c":45,
            "d":75}
sum = 0
for val in students.values():
    if type(val)==int:
        sum+=val
print(sum)

