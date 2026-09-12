import math
side1 =10 
side2 = 9 
perimeter = 36
side3 = perimeter - (side1+side2)
semi_perimeter = (side1+side2+side3)/2
r=semi_perimeter*(semi_perimeter - side1)*(semi_perimeter - side2)*(semi_perimeter - side3)
area = math.sqrt(r)
print(f"area of triangle is : {area}")
