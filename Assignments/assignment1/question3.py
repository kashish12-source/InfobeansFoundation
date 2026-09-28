
tile_length = 13
room_length = 520
tile_breadth = 7
room_breadth = 140

tile_area = tile_length * tile_breadth
room_area = room_length * room_breadth

print(f"no. of tiles required is : {room_area // tile_area}")
