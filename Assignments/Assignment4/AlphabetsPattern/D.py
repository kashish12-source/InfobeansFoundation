# for i in range(1,7):
#     for j in range(1,7):
#         if (i==1  ) or (i==6 ) or j==2   :
#             print("*",end="")
#         elif( j==6 and i!=1 )or (j==6 and i!=6):
#             print("*",end="")
           
#         else:
#             print(" ",end="")
#     print()
# ******
#  *   *
#  *   *
#  *   *
#  *   *
# ******

n = int(input("Enter a no. here : "))
for i in range(1,n):
    k=n-1
    for j in range(1,k):
        if j==1  or (i==1 and j<k-1) or (i==n-1 and j<k-1) or j==k-1 and (i>1 and i<n-1):
            print("*",end="")
        else:
            print(" ",end="")
    print()
# *****
# *    *
# *    *
# *    *
# *    *
# *    *
# *****