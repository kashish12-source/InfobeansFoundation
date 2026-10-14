# 13. Check whether a dictionary is empty.

d ={}
d1 = {1:"23",2:"34"}
count = 0
for val in d1.items():
    count+=1
if count !=0:
    print("Dict is not empty")
else:
    print("Dict is empty")