# Q19. A cube with an edge of 7 cm and a cuboid measuring 7 cm × 4 cm × 8 am are kept on a table.
#  Which shape has more volume?

edge = 7 
cube_volume = edge **3

#volume of cuboid 
length = 7
breadth = 4
height = 8

cuboid_volume = length * breadth * height 

print("Volume of cube =", cube_volume, "cm^3")
print("Volume of cuboid =", cuboid_volume, "cm^3")

if cube_volume > cuboid_volume:
    print("Cube has more volume.")
else:
    print("Cuboid has more volume.")

