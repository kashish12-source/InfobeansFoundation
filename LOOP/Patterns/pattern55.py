n=5
for i in range(1,6):
    l=1
    k = 65
    for j in range(1,10):
        if(j<=n-i):
            print(" ",end="")
        else:
            if(l<=i*2-1):
                l+=1
                print(chr(k),end="")
                k+=1
    print()