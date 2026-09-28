# Q29. How many square tiles of side 10 cm will be required to tile a floor measuring 800 cm by 900 cm?

floor_length = 800
floor_breadth = 900
tile_side = 10

# Area of floor--
floor_area = floor_length * floor_breadth

# Area of one tile
tile_area = tile_side * tile_side

# Number of tiles
total_tiles = floor_area / tile_area

print("Number of tiles required =", int(total_tiles))
