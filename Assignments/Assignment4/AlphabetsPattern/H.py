n = int(input("Enter a no. here : "))
for i in range(1,n):
    for j in range(1,n-1):
        if j==1 or j==n-2 or (i==n//2 and (j<n-2)):
            print("*",end="")
        else:
            print(" ",end="")
    print()

# for i in range(1,8):
#     for j in range(1,7):
#         if i==4 or j==1 or j==6:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
# *    *
# *    *
# *    *
# ******
# *    *
# *    *
# *    *