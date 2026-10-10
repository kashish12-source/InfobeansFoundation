n=int(input("Enter a no. here : "))
for i in range(1, n):
    for j in range(1, n-2):

        if j == 1:
            print("*", end="")

        elif i == 1 or i == n//2 or i == n-1:
            print("*", end=" ")

        else:
            print(" ", end="")

    print()

# ** * * * 
# *    
# *    
# ** * * * 
# *    
# *    
# ** * * * 
