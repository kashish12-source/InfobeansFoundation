# Find occurance of an integer number in array.
arr =[1,1,1,2,2,2,2,3,3,4,5,6,6,6,7,8,8]
integer = 6
count=0
for i in arr:
    if i ==integer:
        count+=1

print(f"The no. of occurance of {integer} in an array is : {count}")