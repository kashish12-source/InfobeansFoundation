# Q.2 Find minimum and maximum element in array
arr = [1,2,3,5,7,9,10]
# here we have the sorted data 
max =0
min = arr[0]
for i in range(1,len(arr)):
    if arr[i]<min:
        min = arr[i]
    elif arr[i]>max:
        max = arr[i]
print(max)
print(min)