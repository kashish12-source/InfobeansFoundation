for i in range(1,8):
    for j in range(1,8):
        if i==1 or i==7 :
            print("-",end="")
        elif j==1 or j==7 :
            print("|",end="")
        elif i==4 and j==4:
            print("X",end="")
        elif i==j :
            print("\\",end="")
        elif i+j==8:
            print("/",end="")
        else:
            print(" ",end="")
   
    print()

# -------
# |\   /|
# | \ / |
# |  X  |
# | / \ |
# |/   \|
# -------