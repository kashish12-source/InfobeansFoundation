n = int(input("Enter a no. here : "))

if n%2==0:
    for i in range(1,n):
        for j in range(1,n):
            if i==1 or j==n//2:
                print("*",end="")
            else:
                print(" ",end="")
        print()
else:
    print(" Enter an even no. here ")
# *******
#    *
#    *
#    *
#    *
#    *
#    *