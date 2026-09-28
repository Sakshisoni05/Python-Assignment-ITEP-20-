# Wall dimensions in metres
wall_length = 20
wall_height = 2
wall_thickness = 0.75

# Brick dimensions in metres
brick_length = 0.25
brick_width = 0.10
brick_thickness = 0.075

# Volume of wall
wall_volume = wall_length * wall_height * wall_thickness

# Volume of one brick
brick_volume = brick_length * brick_width * brick_thickness

# Number of bricks required
number_of_bricks = wall_volume / brick_volume

# Cost: $900 per 1000 bricks
cost = (number_of_bricks / 1000) * 900

print("Number of bricks =", number_of_bricks)
print("Cost =", cost)