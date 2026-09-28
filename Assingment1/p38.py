# 38. The cylinder has a volume of 1287. 
# The base has a radius 10. What is the area of the surface of the cylinder?


import math

volume = 1287
radius = 10

# Find height
# volume = π * r² * h
# height = volume / (π * r²)
height = volume / (math.pi * radius ** 2)

# Total surface area
surface_area = 2 * math.pi * radius * (radius + height)

print("Height =", height, "cm")
print("Surface area =", surface_area, "cm^2")