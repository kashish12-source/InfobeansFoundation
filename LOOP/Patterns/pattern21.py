for i in range(7,1,-1):
    if(i%2!=0):
        for j in range(1,i):
            print(j,end =" ")
        
    else:
        for j in range(i-1,0,-1):
            print(j,end=" ")
    print()
        
