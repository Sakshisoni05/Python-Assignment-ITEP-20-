# Q3. How many tiles whose length and breadth are 13 cm and 7 cm respectively
#  are needed to cover a rectangular region whose length and breadth are 520 cm and 140 cm? 
tile_length = 13
tile_breadth = 7
area_of_tile = tile_length*tile_breadth

print(f"Area of tile= {area_of_tile}")
length =520
breadth = 140

area_of_rectangle = length * breadth 
print(f"Area of rectangle = {area_of_rectangle}")

tile_required = area_of_rectangle / area_of_tile
print(f'Total tile required = {tile_required}')