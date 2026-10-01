# Find the Union and Intersaction of two sorted array.
# Given two arrays a[] and b[] of size n and m respectively. The task is to find union between these two arrays. 
# Union of the two arrays can be defined as the set containing distinct elements from both the arrays. If there are repetitions, then only one occurrence of element should be printed in the union.
# # 

arr1 = [1,2,3,4,5]
arr2= [2,3,4,5,6,7,8,9]

i=0
j=0

a = len(arr1)
b = len(arr2)
greater =(a+b)-1
# union
while(i<a and j<b):
    if arr1[i]!=arr2[j] and arr1[i]>arr2[j]:
        greater+=1
        j+=1
        
    elif arr1[i]!=arr2[j] and arr1[i]<arr2[j]:
        greater+=1
        i+=1
    else:

        greater -=1
        i+=1
        j+=1
inter=0
i=0
j=0
# intersection
while(i<a and j<b):
    if arr1[i] == arr2[j] :
        inter+=1
        j+=1
        i+=1
    elif  arr1[i]<arr2[j]:
        i+=1
    else :
        j+=1
print(inter)

print(f"no. of intersection elements among two array is : {inter}")

print(f"no. of elements in union of two array is : {greater}")
