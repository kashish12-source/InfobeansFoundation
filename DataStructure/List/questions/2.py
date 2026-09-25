l=[2,3,4,5,7,6]
target = 38
for i in range(len(l)):
    if (l[i]==target):
        print(f"Element found at index : {i+1}")
        break
else:
    print("Element not found ")