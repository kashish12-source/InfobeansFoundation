for i in range(1,6):
    for j in range(i):
        if(i%2==0):
            if(j%2!=0):
                print("1",end="")
            else:
                print("0",end ="")
        else:
            if(j%2==0):
                print("1",end="")
            else:
                print("0",end ="")
    print()