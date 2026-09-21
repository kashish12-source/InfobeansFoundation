k = 65+32
for i in range(1,6):
    
    for j in range(1,6):
        if i==j or i==5 or j==1:
            print(chr(k),end="")
            k+=1
        else:
            print(" ",end="")
            

   
    print()
