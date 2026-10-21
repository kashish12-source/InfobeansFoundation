# Given an unsorted array arr[] of size N having both negative and positive integers. The task is place all negative element at the end of array without changing the order of positive 
arr = [1, -1, 3, 2, -7, -5, 11, 6]
negative =[]
positive = []
for i in arr:
    if i<0:
        negative.append(i)
    else:
        positive.append(i)
res = positive+negative
print(res)