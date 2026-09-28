# 33. A rectangular garden has dimensions of 30 m by 20 m 
# and is divided in to 4 parts by two pathways that run perpendicular from its sides.
# One pathway has a width of 3 m and the other, 4 m. Calculate the total usable area of the garden.

# Dimensions of the garden
length = 30
width = 20
garden_area = length * width
print(f"Area of the garden = {garden_area}m^2")

# Dimensions of the pathways
pathway1_width = 3
pathway2_width = 4

# Calculate the area of each pathway
pathway1_area = length * pathway1_width
pathway2_area = width * pathway2_width

# Calculate the total usable area of the garden
usable_area = garden_area - pathway1_area - pathway2_area
print(f"Total usable area of the garden = {usable_area}m^2")

