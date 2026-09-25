n=5
for i in range(1,6):
    for j in range(5,0,-1):
        if(j>i):
            print(" ",end="")
    for j in range(i,0,-1):
        print(j,end="")
    
    k=2
    for j in range(i-1):
        print(k,end="")
        k+=1
    print()
        
#     1
#    212
#   32123
#  4321234
# 543212345
