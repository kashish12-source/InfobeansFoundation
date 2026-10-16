# 30. Safely retrieve a value from a deeply nested dictionary. If any key is
#     missing, return a default value such as "Unknown".

student = {
    "name": "Kashish",
    "details": {
        "education": {
            "college": "IIST",
            "year": 3
        }
    }
}
result = student.get("","unknown")
print(result)