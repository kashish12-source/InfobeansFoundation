# n = 20
# org = n
# res = ""

# while(n != 0):
#     dig = n % 2
#     res = str(dig) + res  
#     n = n // 2

# print(res) 


k=1 
for i in range(1,6):
    for j in range(5,0,-1):
        if j>i:
            print(" ",end="")
    for j in range(2*i-1):
        if j==i-1:
            print("#",end="")
            
        else:
            print("*",end="")
    print()

for i in range(1,8):
    if i<=4:
        k=1
        for j in range(4,0,-1):
            if i<j:
                print(" ",end="")
            else:
                print(k,end="")
                k+=1
        print()
    else:
        k=1
        for j in range(5,9):
            
            if i>=j :
                print(" ",end="")
            else:
                print(k,end="")
                k+=1
        print()


k=5
for i in range(1,8):
    if i<=4:
        for j in range(4,0,-1):
            if j>i:
             print(" ",end="")        
        for j in range(1,2*i):
            if j%2==0:
                print("_",end="")
            else:
                print("*",end="")
        print()
    else:
        for j in range(5,9):
            if i>=j:
                print(" ",end="")
        for j in range(1,2*(8-i)):
            if (j%2==0):
                print("_",end="")
            else:
                print("*",end="")
        print()
k=4
for i in range(1,6):
    for j in range(1,11):
        if j<=i and j<6:
            print('*',end="")
       
        elif j>=6 and j<=10-k:
            print("*",end="")
        else:
            print(" ",end="")
    k-=1

    print()


k = 4 
for i in range(1,6):
    for j in range(1,11):
        if j<=i and j<6:
            print("*",end="")
        elif j>=6 and j<=10-k:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    k-=1


for i in range(1,6):
    for j in range(5,0,-1):
        if i<j:
            print(" ",end="")
    for j in range(2*i-1):
        if j%2!=0:
            print(0,end="")
        else:
            print(1,end="")
    print()
for i in range(1,6):
    for j in range(5,0,-1):
        if i<j:
            print(" ",end="")
    for j in range(1,2*i):
        if i==j :
            print("#",end="")
        else:
            print("*",end="")
    print()

for i in range(1,8):
    if i<=4:
        for j in range(1,5):
            if j<=i:
                print(j,end="")
            else:
                print(" ",end="")
        print()
    else:
        for j in range(1,(8-i)+1):
            print(j,end="")
        print()