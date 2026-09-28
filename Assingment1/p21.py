# 21. A brick measures 15 cm in length, 8 cm in breadth and 5 cm in height.
# How many bricks will be used to make a wall of length 15 m, breadth 10 m and height 8 metres?

#----Brick-----
length =15
breadth = 8
height =5

#----wall-------
w_length =15
w_breadth = 10
w_height = 8

#---meter to centimeter ---
w_length = w_length*100
w_breadth= w_breadth*100
w_height = w_height *100

#volume of brick
brick_volume= length * breadth * height

#volume of wall...
wall_volume = w_length * w_height * w_breadth

#number of bricks--
total = wall_volume / brick_volume

print(f"Total number of bricks use : {total}")

