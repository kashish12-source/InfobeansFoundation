# Sub with equal 0s and 1s
# Given an array containing 0s and 1s. Find the number of subarrays having equal number of 0s and 1s. 
# Example 1:
# Input:
# n = 7
# A[] = {1,0,0,1,0,1,1}
# Output: 8
# Explanation: The index range for the 8 
# sub-arrays are: (0, 1), (2, 3), (0, 3), (3, 4), 
# (4, 5) ,(2, 5), (0, 5), (1, 6)
# Example 2:
# Input:
# n = 5
# A[] = {1,1,1,1,0}
# Output: 1
# Explanation: The index range for the 
# subarray is (3,4).

arr = [1,0,0,1,0,1,1]

res = 0

for i in range(len(arr)-1):

    count_1 = 0
    count_0 = 0

    for j in range(i, len(arr)):

        if arr[j] == 1:
            count_1 += 1

        else:
            count_0 += 1

        if count_1 == count_0:
            res += 1

print(res)