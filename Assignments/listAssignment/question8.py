# Q.7 Sub array with given sum
# let us assume that the array is sorted in increasing order 
arr =[1,2,3,7,5]
current_sum = 0
target = 12
left = 0
right = 0
while(left<=right):
    current_sum += arr[right]
    while(current_sum>target and left<right ):
        current_sum -= arr[left]
        left +=1
    if current_sum == target:
        print(f"{left+1} , {right+1}")
    right+=1
