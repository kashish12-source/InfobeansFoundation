n=5
for i in range(1,6):
    k=1
    for j in range(1,10):
        if(j<=n-i):
            print(" ",end="")
        else:
            if(k<=2*i-1):
                print(k,end="")
                k+=1
    print()

#     1
#    123
#   12345
#  1234567
# 123456789