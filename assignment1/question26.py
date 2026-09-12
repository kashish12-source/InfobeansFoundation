brick_length = 0.24
brick_width = 0.15

length = 120 
breadth = 2.4

area_path = length * breadth 

area_brick = brick_length*brick_width

brick_required = area_path // area_brick

print(f"brick required to cover the path is : {brick_required}")
