# Q12. Find the area of a right angled triangle whose hypotenuse is 13 cm and 
# one of its sides containing the right angle is 12 cm. Find the length of the other side.

# pythagorous theorem
# h^2 = b^2 + p^2
# 13^2 = 12^2 + p^2
# 169 = 144 + p^2
# p^2 = 125
# p=5

import math

hypotenues = 13
side1 = 12

side2 = math.sqrt(hypotenues**2 - side1**2)

# Area = 1/2 × base × height
area = 0.5 * side1 * side2

print("Other side =", side2, "cm")
print("Area of triangle =", area, "cm^2")
