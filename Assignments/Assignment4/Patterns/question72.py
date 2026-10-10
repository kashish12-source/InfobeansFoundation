for i in range(1,8):
    if i<=4:
        for j in range(1,i+1):
            print(j,end="")
        print()
    else:
        for j in range(1,8-i+1):
            print(j,end="")
        print()


1
12
123
1234
123
12
1