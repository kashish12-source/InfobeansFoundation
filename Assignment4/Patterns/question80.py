k=1
for i in range(5,0,-1):
    for j in range(1,11):
        if i>=j:
            print("*",end="")
        elif j>=6 and j<=11-k:
            print("*",end="")
        else:
            print(" ",end="")
    k+=1
    print()
# **********
# **** **** 
# ***  ***  
# **   **   
# *    *    