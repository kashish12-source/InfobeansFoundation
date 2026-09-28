length = 0.25
breadth = 0.1
height =0.075

volume_brick = length*breadth*height 

length = 20
breadth = 2
height = 0.75

volume_wall = length * breadth * height 

bricks_required = volume_wall / volume_brick

print(f"cost required is : ${bricks_required*0.9}")