#26. How many bricks will be required to lay a path 120 m long and 2.4 m breadth
#  if a brick is 24 cm long and 15 cm wide?


#  Path:

Length = 120 
Breadth = 2.4 
# meter to centimeter--
Length = 120 *100
Breadth = 2.4* 100

#brick 
Length_brick = 24
breadth_brick =15

path_area = Length * Breadth 

# area of one brick
brick_area=  Length_brick * breadth_brick

total = path_area / brick_area

print(f'{total} bricks will be required')