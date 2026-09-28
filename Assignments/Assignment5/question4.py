# Q.4 Write a program to sort the array

arr =[2,3,1,4,8,5,6]

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]>arr[j]:
            arr[i],arr[j] = arr[j],arr[i]
print(arr)

# its time complexity is O(n**2)
# to solve this problem in nlogn  we need to use merge sort 
