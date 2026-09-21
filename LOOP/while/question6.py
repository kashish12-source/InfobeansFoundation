# # n=1234
# # res = 0
# # while(n!=0):
# #     dig = n%10
# #     res = res*10 + dig
# #     n = n//10
# # print(res)


# # print("armstrong no.")
# # n=153
# # i = 0

# # org = n
# # while(n!=0):
# #     i+=1
# #     n=n//10
# # # print(i)
# # n=org
# # res = 0
# # while(n!=0):
# #     dig = n%10
# #     res += dig ** i
# #     n = n//10
# # if(org == res):
# #     print("armstrong")
# # else:
# #     print("not armstrong")
    
# # print()
# # print("check palindrome no. ")

# # n = 121
# # org = n

# # res = 0 
# # while(n!=0):
# #     dig = n%10
# #     res =res*10 + dig 
# #     n = n//10
    
# # if ( res == org ):
# #     print("Palindrome ")
# # else:
# #     print("not palindrome ")


# # n = 5
# # for i in range (1,n+1):
# #     if(n%i==0):
# #         print(i)


# n=6
# t1=0
# t2=1

# if n>2:
#     print(t1,end=" ")
#     print(t2,end=" ")
#     while(n!=0):
#         k = t1+t2
#         print(k,end =" ")
#         t1=t2
#         t2=k
#         n-=1

# else:
#     print("please enter two no. ")

# for i in range(65,91):
#     print(chr(i+32),end = " ")
# n=4
# i=1
# j=2
# if(n>2):
#     print(i,end = " ")
#     print(j,end ="       ")
#     while(n!=0):
#         k = i*j
#         print(k,end=" ")
#         i=j
#         j = k 
#         n-=1
# else:
#     print("enter no. greater than 2")
# sum =0
# for i in range(1,n):
#     if(n%i==0):
#         sum+=i
# if(sum == n):
#     print("perfect no. ")
# else:
# #     print("not perfect")

# n=123
# count= 0
# while(n!=0):
#     n = n//10
#     count+=1
# print(count)

# n = 144
# org = n 
# res = 0
# while(n!=0):
#     dig = n%10
#     fact = 1
#     for i in range(2,dig+1):
#         fact *=i
#     res+=fact 
#     n=n//10
# if(res == org):
#     print("strong")
# else :
#      print("not strong")


n =12
if n%3==0:
    for i in range (-n,n+1,3):

        print(i,end =" ")
else:
    print("enter the even no. which is divisible by 3")