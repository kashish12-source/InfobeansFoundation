for i in range(1,10):
    for j in range(1,10):
        if i==5 and j<=5:
            print(j,end="")
        if j==5 and i<5:
            print(i,end="")
        if i== 5 and j>5:
            print(10-j,end="")
        if j==5 and i>5:
            print(10-i)
        else:
            print(" ",end="")
        
    print()
        
    