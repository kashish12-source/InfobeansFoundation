# Print all keys, all values, and all key-value pairs of a dictionary.

d1 = {
    "1":23,
    "2":35,
    "3":45
}
print("Here is the values ",end=" ")

for val in d1.values():
    print(val,end="  ")

print()
print("Here is the keys : ",end=" ")
for key in d1.keys():
    print(key , end=" ")
print()
print("Here is the key value pairs : ",end=" ")
for key , value in d1.items():
    print(f"({key},{value})",end=",")
