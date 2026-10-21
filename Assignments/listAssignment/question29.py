# Suppose a one-dimensional array AR containing integers is arranged in ascending order. Write a java program to search for an integer from AR with the help of Binary search method, 
arr =[1,2,3,4,5,6,7,8,9]
target = 80
start = 0
end = len(arr)-1

f=False
while start <= end:

    mid = (start + end) // 2

    if arr[mid] == target:
        f = True
        break

    elif arr[mid] > target:
        end = mid - 1

    else:
        start = mid + 1

if f:
    print("Element found")
else:
    print("Element not found ")