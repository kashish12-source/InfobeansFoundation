k=1
for i in range(1,10):
    if(i%2!=0):
        for j in range(0,i):
            print(k,end ="")
        k+=1
        i+=2
    else:
        continue
    print()