# Find the second-largest distinct value in a dictionary.

d = {1,2,4,3,4,3,5,6,8,6,8,3,1,10}
s= set()
for i in d:
    s.add(i)
l = []
for i in s:
    l.append(i)

print(s)
if len(l)>=2:
    for i in range(len(l)-1):
        if i == len(l)-2:
            print(l[i])
else:
    print("The dictionary only have one element so it is not possible to find the second largest element ")
