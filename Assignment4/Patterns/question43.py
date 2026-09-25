n=5

for i in range(1,6):
    
    for j in range(5,0,-1):
        if(i==j) or i==5 or j==1:
            print("1",end="")
        else:
            if i<j:
                print(" ",end="")
            else:
                print("*",end="")
    print()
