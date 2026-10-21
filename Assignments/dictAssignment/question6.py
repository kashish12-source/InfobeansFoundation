# 6. Remove a key from a dictionary using pop(). Handle the case where the
#    key does not exist.

students = {"name":"kashish","branch":"CSE","contact":7489619180,"marks":96}

key ="marks"
for k in students.keys():
    if k == key:
        students.pop(k)
        print(f"after delteing a key the values of dict is : {students}")
        
        break
else:
    print("Key is not present in the dict ")

