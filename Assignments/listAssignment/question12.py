arr = [1,5,7,1]
k =6
count =0
for i in range(len(arr)):
    
    for j  in range(i+1,len(arr)):
        if arr[i]+arr[j] ==k:
            count+=1
print(count)