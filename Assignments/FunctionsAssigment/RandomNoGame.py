# 5. Number Guessing Game
# Beginner
# Concepts: while, if-else, functions
# Requirements
# •	Generate a random number from 1 to 100.
# •	Ask the player to guess the number.
# •	Display “Too high” or “Too low.”
# •	Limit the player to seven attempts.
# •	Display the final result.
# Bonus: Add easy, medium, and hard difficulty levels with different attempt limits.


import random as ran

def generating_number():
    num = ran. randint(1,100)
    return num
f = True
sum =0
while(f):
    print()
    print("Press 1 to start the game")
    print("Press 2 to end the game")
    print()

    choice = int (input("Enter your choice here : "))
    if choice == 1:
        
        i=7 
        num = generating_number()
        guessed = False
        while(i!=0):
            n = int(input("Enter a number here : "))
            if n < num:
                print("Too low")
            elif n >num :
                print("Too high")
            else:
                print("Correct")
                guessed=True
                sum+=1
                break
            i-=1
        if not guessed:
            print(f"Game over the correct answer is : {num}")

    elif choice ==2:
        f = False

    else:
        print("Enter the valid choice")

print(f"your score is : {sum}")
