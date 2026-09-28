# # 39. Find the surface of the cylinder if its diameter is 12 centimeters and its height is 9 centimeters.

# diameter = 12
# height = 9

# radius = diameter /2

# # surface area = 2 pi r ( h+r)
# surface_area = 2 * 3.14159 * radius * (height + radius)
# print(f"Surface area of the cylinder = {surface_area} cm^2")    

import math

diameter = 12
height = 9

# Find radius
radius = diameter / 2

# Total surface area
surface_area = 2 * math.pi * radius * (radius + height)

print("Radius =", radius, "cm")
print(f"surface area of the cylinder = {surface_area} cm^2")
