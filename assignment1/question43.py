import math
height = 4 
slant = 5 
rate = 10

r = math.sqrt(slant**2 - height **2)
area = 3.14 * r**2

cost = area * rate 
print(f"cost is : ${cost}")