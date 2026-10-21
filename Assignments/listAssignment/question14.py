# Find the first repeating element in array of integers
arr = [1,5,3,3,5,7,6,6,9]
if len(arr)==1:
    print("No repeating elements their")

else: 
    f=False
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i]==arr[j]:
                print(arr[i])
                f=True
        if f:
            break
        