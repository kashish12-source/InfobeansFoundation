length = 5
breadth = 8
tile_area = length * breadth 
length = 200
breadth = 400
room_area = length * breadth 

tile_required = room_area / tile_area

print(f"tiles required to cover the room is : {tile_required}")