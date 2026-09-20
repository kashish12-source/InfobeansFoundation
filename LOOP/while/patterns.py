# # for i in range (1,4):
# #     for j in range(1,4):
# #         print(i ,j)
# #     print()
    
# for _ in range(5):
#     for _ in range(5):
#         print("*",end=" ")
#     print()
# print("\n")
# # *
# # **
# # ***
# for i in range(1, 5):
#     for j in range(i):
#         print("*",end = " ")
#     print()

# print("\n")


# # *****
# # ****
# # ***
# # **
# # *
# for i in range(5,0,-1):
#     for  j in range(0,i):
#         print("*",end =" ")
#     print()


# # * 
# #  *
# #   *
# #    *
# #     *
# #      *

# print("\n")
# for i in range (5):
#     for j in range(5):
#         if(i==j):
#             print("*",end ="")
        
#         print(" ", end = "")
#     print()
    
#     *
#    **
#   ***
#  ****
# *****
# for i in range(5,0,-1):
#     for j in range(0,i-1):
#         print(" ",end="")
#     for k in range(5,i-1,-1):
#         print("*",end="")
        
#     print()
for i in range(1,6):
    for j in range(5,i,-1):
        print(" ",end="")
    for k in range(1,i+1):
        print("*",end="")
    for l in range(1,i):
        print("*",end="")
    print()
    
    
for i in range(9):
    for j in range(9):
        if i==4 or j == 4:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    
print("\n\n\n")

for i in range(9):
    for j in range(9):
        if (j==0 and i<4) or (i==0 and j>4) or (i==8 and j<4 )or (j==8 and i>4)or (i==4)or j==4:
            print("@",end="")
        else:
            print(" ",end = "")
    print()
    
print("\n\n\n\n")
for i in range(5,0,-1):
    for j in range(1,11):
        if (j>i and j<=(10-i)):
            print(" ",end="")
        else:
            print("*",end ="")
    print()

