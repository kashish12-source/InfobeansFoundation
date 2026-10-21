# An element is called a peak element if its value is not smaller than the value of its adjacent elements(if they exists).
# Given an array arr[] of size N, find the index of any one of its peak elements.
# Note: The generated output will always be 1 if the index that you return is correct. Otherwise output will be 0.

arr = [1,24,3,56,86,9,7]
if len(arr) == 1 or arr[len(arr)-1]>arr[len(arr)-2]:
    print(1)
    
else:
    for i in range(len(arr)-2):
        if (i==0) and arr[i]>arr[i+1]:
            print(1)

        if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
            print(1)
            break
    else:
        print(0)