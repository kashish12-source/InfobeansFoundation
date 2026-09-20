# # n=5
# # i=1
# # sum = 0
# # while(i<=n):
# #     sum+=i
# # #     i+=1
# # # print(sum)
# # n = 5
# # result = 1
# # while(n>=2):
# #     result*=n
# #     n-=1
# # print(result)

# # n =6
# # i =2 
# # f = False
# # while(i<=n//2):
# #     if(n%i==0):
# #         f= True
# #     i+=1
# # if(f):
# #     print("Not a prime")
# # else:
# #     print("a prime")


# # fibonacci
# # l=0
# # i =0 
# # j = 1
# # print(i)
# # print(j)
# # while(l<=n-3):
# #     k=i+j
# #     print(k)
# #     i=j
# #     j=k
# #     l+=1

# # j=0
# # i=1
# # n=6
# # while(n!=0):
# #    k=i+j
# #    print(k)
# #    i=k
# #    j=j+1
# #    n=n-1

# n =8
# # i=1
# # while(n!=1):
# #     if(i==1):
# #         print(f"{i} + ",end="")
# #     else:
# #         print(f"1/{i} + ",end=" ")
# #     i +=1
# #     n-=1
# # print(f"1/{i}")
# # i=0
# # while(n!=0):
# #     print(i*7,end=" ")
# #     i+=1
# #     n-=1
# # i=1
# # while(n!=0):
# #     print(f"{i**3}",end=" ")
# #     i+=2
# #     n-=1

# i=2
# f = False
# while(i<=n//2):
#     if(n%i==0):
#         f=True
#         break
#     i+=1
# if(f)or n<2:
#     print("not prime")
# else:
#     print("prime")



# n = 5
# sum=0
# for i in range(1,n+1):
#     sum+=1/i
# print(f"{sum:.2f}")
# n= 123
# result=0
# for _ in range (len(str(n))):
#     dig = n%10
#     result = result*10+dig
#     n = n//10

# print(result)

# check palindrome


# get the no. x**y
# x = 10
# y = 5
# res = 1
# for i in range (1 , y+1):
#     res *= x

# print(res)




# armstrong no. 
n =154
org = n 
res = 0 
power = len(str(n))
for _ in range (len(str(n))):
    dig = n%10
    res += dig ** power
    n = n//10
if(org == res ):
    print("armstrong")
else : 
    print( " not armstrong ")

    
# sum of all the digits of an integer 

n = 123
res = 0 
for i in range (len(str(n))):
    dig = n %10
    res += dig 
    n = n//10
print(res)

# perfect no. 
n=6
i =1 
res = 0 
while i <=n //2:
    if(n%i==0):
        res += i
    
    i+=1
if(res == n ):
    print("perfect no. ")
else:
    print("not a perfect no. ")

    # count no .of digits
n=4235
count = 0
for _ in (str(n)):
    count+=1
print(count)   

# check for strong no. 

n =146
org = n
res = 0
for i in range(len(str(n))):
    dig = n%10
    x = 1
    for j in range(2,dig+1):
        x*=j
    res+=x
    n=n//10
if(res == org):
    print("strong")
else:
    print("not strong")


n = 123545
even=0
n_str= str(n)
odd =0
for i in range(len(str(n))):
    if int(n_str[i])%2==0:
        even+=1
    else:
        odd+=1
print(odd)
print(even)
