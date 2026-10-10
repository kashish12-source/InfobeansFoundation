k=4
for i in range(1,6):
    for j in range(1,11):
        if j<=i and j<6:
            print('*',end="")
       
        elif j>=6 and j<=10-k:
            print("*",end="")
        else:
            print(" ",end="")
    k-=1

    print()
# *    *    
# **   **   
# ***  ***  
# **** **** 
# **********