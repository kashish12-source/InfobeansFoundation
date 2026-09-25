l=[1,2,3,4,5,7,6]
target = 10
start =0
end =len(l)-1
while(start<end):
    l[start],l[end]=l[end],l[start]
    start+=1
    end-=1
print(l)

    