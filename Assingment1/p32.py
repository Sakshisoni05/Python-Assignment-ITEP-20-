# 32. A square garden with a side length of 150 m 
# has a square swimming pool in the very centre with a side length of 25 m .
#  Calculate the area of the garden.


# Area of the garden
garden_side = 150

garden_area = garden_side * garden_side
print(f"Area of the garden = {garden_area}m^2")

# Area of the swimming pool
pool_side = 25
pool_area = pool_side * pool_side
print(f"Area of the swimming pool = {pool_area}m^2")

# Area of the garden excluding the swimming pool
garden_area_excluding_pool = garden_area - pool_area
print(f"Area of the garden excluding the swimming pool = {garden_area_excluding_pool}m^2")

