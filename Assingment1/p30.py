#30. How many tiles of length 5cm and breadth 8cm are needed
#  to tile the floor of a bed room 200 cm long and 400 cm wide?

# tile --
tile_length = 5
tile_breadth = 8

# bed room ---
room_length = 200
room_breadth = 400

# Area of bed room
room_area = room_length * room_breadth  

# Area of one tile
tile_area = tile_length * tile_breadth  

# Number of tiles
total_tiles = room_area / tile_area

print("Number of tiles required =", int(total_tiles))   




