# # 37. The surface of the cylinder is 149 cm².
# # The cylinder height is 6 cm. What is the diameter of this cylinder?

# area = 149
# height = 6

# # surface area = 2πr(h+r)
# # 149 = 2 * 3.14159 * r * (6 + r)
# # 149 = 6.28318 * r * (6 + r)
# # 149 = 6.28318 * r * 6 + 6.28318 * r^2
# # 149 = 37.69908 * r + 6.28318 * r^2

# # 6.28318 * r^2 + 37.69908 * r - 149 = 0


# a = 6.28318
# b = 37.69908
# c = -149

import math

surface_area = 149
height = 6

# 149 = 2πr(r + 6)
# Solve the quadratic equation:
# r² + 6r - 149/(2π) = 0

a = 1
b = height
c = -surface_area / (2 * math.pi)

r = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)

diameter = 2 * r

print("Radius =", r, "cm")
print("Diameter =", diameter, "cm")
