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

arr = [1,2,42,6,47,3,4,8]
target = 1
for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        if arr[i]>arr[j]:
            arr[i],arr[j] = arr[j],arr[i]
print(arr)
f=False
if len(arr)>=2:
    if arr[0] == target:
        print(f"The no. itself is the smallest one hence the lesser no. does not exists\nbut the greater no. is {1}")
        f = True
        
    
    elif arr[len(arr)-1] == target:
        print(f"The no. is iteself a greater no. hence only the smaller no. will exists i.e = {arr[len(arr)-2]}")
        f=True
        
    else:
        for i in range(len(arr)):
            if arr[i]==target:
                print(f"Lesser is {arr[i-1]}")
                print(f"Greater is {arr[i+1]}")
                f=True
                break
    if not f:
        print("Target element does not exist in the array")
else:
    print("their must me more than 2 no. ")
