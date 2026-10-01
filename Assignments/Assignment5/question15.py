# Find the first non-repeating elment in given array of integers
# Find the first non-repeating element in a given array arr of N integers.
# Note: Array consists of only positive and negative integers and not zero.
# Example 1:
# Input : arr[] = {-1, 2, -1, 3, 2}
# Output : 3
# Explanation:
# -1 and 2 are repeating whereas 3 is 
# the only number occuring once.
# Hence, the output is 3.

arr = [-1, 2, -1, 3, 2]
for i in range(len(arr)-1):
    count=0
    for j in range(len(arr)):
        if arr[i]==arr[j]:
            count+=1
    if count == 1:
        print(arr[i])
        break