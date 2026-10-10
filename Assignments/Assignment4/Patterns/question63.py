for i in range(1,6):
    
    for j in range(5,0,-1):
        if i<j:

            print(" ",end="")
    for j in range(2*i-1):
        if j==i-1:
            print("#",end="")
        else:
            print("*",end="")
    print()


#     #
#    *#*
#   **#**
#  ***#***
# ****#****