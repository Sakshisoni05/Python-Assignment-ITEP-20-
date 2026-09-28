# 43. Find the cost of polishing the base of a cone 
# whose height is 4cm and slant height 5 cm at the rate of 10 rs. Per sq. cm

import math

height = 4
slant_height = 5

#Find radius using pythagoras theorem
# r^2 + h^2 = l^2
# r^2 = l^2 - h^2
# r = sqrt(l^2 - h^2)
radius = math.sqrt(slant_height ** 2 - height ** 2) 

# Area of base = π * r^2
area_of_base = math.pi * radius ** 2

# Cost of polishing = Area of base * Rate per sq. cm
cost_of_polishing = area_of_base * 10

print(f'Cost of polishing the base of the cone = {cost_of_polishing} rs.')

