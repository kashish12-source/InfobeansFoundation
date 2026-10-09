t = (1,2,3)
print(t)

t1 =1,2,3,4,5,6
print(t1)

t2=()
# you can create the empty tuple but with the single value you need to place the "," after that value 

print(type(t2))

t3 = tuple([1,2,3,4,5,6,7,8,99,10])
print(t3)

t4 = (1,2,3,4,5,6)

for i in range(len(t4),0,-1):
    print(i,end=" ")

# slicing in list  : 

print(t4[1:3])


# Tuple Immutability:


# t4[1]=23245
# print(t4)
# Traceback (most recent call last):
#   File "c:\Users\Kashish\infobeans_technical\DataStructure\tuples\creatingTuple.py", line 26, in <module>
#     t4[1]=23245
#     ~~^^^
# TypeError: 'tuple' object does not support item assignment


# if the tuple contain the mutable data in it :
