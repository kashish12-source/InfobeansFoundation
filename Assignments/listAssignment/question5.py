# Find the kth largest and kth smallest element in array
arr = [1,1,2,2,3,4,4,5,6,7,7,8,9,9,10]
k = 3  
# lets remove the duplicate element from the array and then return the kth smallest and kth largest


i=0
j=1
count = 0
for i in range(len(arr)-1):
    if (arr[i] !=arr[i+1]):
        arr[j]=arr[i+1]
        j+=1
        count+=1
print(arr)
print(count)
min = 0
max =count
print(f"{k}th smallest element is : {arr[(min+k-1)]}")
print(f"{k}th largest element is : {arr[(max-k)+1]}")
