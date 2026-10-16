# 28. Create a new dictionary containing only entries whose values are greater
#     than or equal to a given threshold. Do not modify the dictionary while
#     iterating over it.
marks = {
    "Aman": 85,
    "Riya": 45,
    "Karan": 70,
    "Neha": 30,
    "Priya": 90
}
result = {}
threshold = 70
for i in marks.keys():
    if marks[i] >= threshold:
        result[i] = marks[i]
print(result)