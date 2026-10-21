# Write a Java program to swap first and last element of an integer 1-d array.
arr =[2,3,15,6,48,7,5]
if len(arr)>1:
    arr[0] , arr[len(arr)-1] = arr[len(arr)-1],arr[0]
    print(arr)
else:
    print("To swap the first and last element we need atleast two digits ")
