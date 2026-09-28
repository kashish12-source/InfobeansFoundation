base =128
base2 = 92
height = 40 

way =4 
trap_area = ((base + base2 )*height ) / 2

walkway_area = way *height

result = walkway_area+trap_area

print(f"area of the wooden after addition of walkway is : {result}m2")