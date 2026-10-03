#  Write a Java program to find the sum and average of one dimensional integer array. 
arr =[1,2,3,5,67,8,5]
n= len(arr)
sum = 0
for i in arr:
    sum+=i
average = sum/n
print(f"Average of the one Dimensional array is : {average:.2f}")
print(f"Sum of the one Dimensional array is : {sum}")
