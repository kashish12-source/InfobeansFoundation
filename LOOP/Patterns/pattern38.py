
for i in range(5,0,-1):
    k=65
    for j in range(1,i+1):
        if i==5 or j==1 or i==j:
            print(chr(k),end="")
            k+=1
        else:
            print(" ",end="")
            k+=1
    print()
    