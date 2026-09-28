# 34. A wooded area is in the shape of a a trapezoid whose bases measure 128 m and 92 m and its height is 40 m.
# A 4 m wide walkway is constructed which runs perpendicular to the two bases. 
# Calculate the area of the wooded area after the addition of the walkway.

# Dimensions of the trapezoid
base1 = 128
base2 = 92
height = 40

# Calculate the area of the trapezoid
trapezoid_area = (1/2) * (base1 + base2) * height

# Dimensions of the walkway
walkway_width = 4
walkway_length = height

# Calculate the area of the walkway
walkway_area = walkway_width * walkway_length

# Calculate the total area after adding the walkway
total_area = trapezoid_area + walkway_area

print(f"Area of the trapezoid = {trapezoid_area} m^2")
print(f"Area of the walkway = {walkway_area} m^2")
print(f"Total area = {total_area} m^2")

