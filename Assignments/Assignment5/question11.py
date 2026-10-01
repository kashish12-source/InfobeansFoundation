# Write a program to cyclically rotate array by one.

arr = [1,2,3,4,5]
for i in range(len(arr)-1,0,-1):
    arr[i],arr[i-1] = arr[i-1],arr[i]
print(arr)