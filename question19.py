edge = 7
side1 = 7
side3 = 8
side2 = 4

cube_volume =edge**3
cuboid_volume = side1* side2 * side3

if(cube_volume > cuboid_volume):
    print(f"volume of cube is greater i.e : {cube_volume}")
else:
    print(f"volume of cuboid is greater i.e : {cuboid_volume}")
    