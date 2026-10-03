# Write a Java program to find the largest and smallest element of an array.

arr = [2,4,2,53,7,4,7,8]
largest = 0
smallest = arr[0]
if len(arr)>1:
    for i in arr:
        if i>largest:
            largest = i
        elif i<smallest:
            smallest = i
    print(f"The largest element is : {largest}")
    print(f"The smallest element is : {smallest}")
else:
    print("The array you entered contain only one element hece the largest and the smallest element will be the no. itself")