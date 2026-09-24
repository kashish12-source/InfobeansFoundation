# 60) WAP to print Square, Cube and Square Root of all numbers from 1 to N
import math
n= int(input("Enter the no. here : "))

for i in range(1,n+1):
    print(f"square of {i} is {i**2}")
    print(f"cube of {i} is {i**3}")
    print(f"square root of {i} is {math.sqrt(i):.2f}")
    print()