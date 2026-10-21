# 14. Copy a dictionary into another dictionary. Explain whether changing a
#     nested object in the copy can affect the original.
d1 = {
    "1":23,
    "2":35,
    "3":45
}
d2 = d1.copy()
d2["2"] = 435
print(d2)
print(d1)
