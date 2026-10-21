# Write a Java program to reverse the element of an integer 1-D array. 

arr = [1,2,3,4,5,6,7,8,9]
i=0
j = len(arr)-1
if len(arr)>1:
    while(i<j):
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1
    print(arr)
else:
    print("To reverse the array we must need the array of length greater than 1")