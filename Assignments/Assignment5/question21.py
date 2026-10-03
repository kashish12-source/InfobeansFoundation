# Q.20 Longest consecutive sequence.
# Given an array of positive integers. Find the length of the longest sub-sequence such that elements in the subsequence are consecutive integers, the consecutive numbers can be in any order.
#  
# Example 1:
# Input:
# N = 7
# a[] = {2,6,1,9,4,5,3}
# Output:
# 6
# Explanation:
# The consecutive numbers here
# are 1, 2, 3, 4, 5, 6. These 6 
# numbers form the longest consecutive
# subsquence.
# Example 2:
# Input:
# N = 7
# a[] = {1,9,3,10,4,20,2}
# Output:
# 4
# Explanation:
# 1, 2, 3, 4 is the longest
# consecutive subsequence.

arr = [1,9,3,10,4,20,2]
max = 0
for i in range(len(arr)-1):
    count =0
    k=1
    current = arr[i]
    for j in range(i+1,len(arr)):
        
print(max)
