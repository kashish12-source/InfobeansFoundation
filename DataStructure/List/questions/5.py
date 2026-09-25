l =[1,2,3,4,5,6,7]
target = 10
start = 0 
end = len(l)-1
while(start<end):
    if(l[start]+l[end]==target):
        print(l[start])
        print(l[end])
    if 