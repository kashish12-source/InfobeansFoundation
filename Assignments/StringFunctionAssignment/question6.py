# q6. Find the length of a string without using len().
def count_length(s):
    count =0 
    for i in s :
        count+=1
    return count 

s = "abcdfgshsafew"
print(f"The length of the string '{s}' is : {count_length(s)}")
