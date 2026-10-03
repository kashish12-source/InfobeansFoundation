# Q.22) Java program to find nearest lesser and greater element in array
# Given an array of N elements and we have to find nearest lesser and nearest greater element using C program.
# Example:
#     Input:
#     Enter the number of elements for the arrray : 3  
 
#     Enter the elements for array_1.. 
#     array_1[0] : 1   
#     array_1[1] : 2   
#     array_1[2] : 3   
 
#     Enter the number : 2 
 
#     Output:
#     Element lesser than 2 is : 1 
#     Element greater than 2 is : 3

arr = [1,5,8,10,15,4]

n = 8
less =-1
big = -1
for i in range(len(arr)):
    if arr[i]<n:
        less = arr[i]
    if arr[i]>n:
        if (big - n)<big:
            big = arr[i]
print(less )
print(big)