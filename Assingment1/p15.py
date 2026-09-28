# Q15. Shelly has a rectangular garden of length 22 m and breath 15 m. 
# Her friend Rachel has a square garden of side 21 m. Whose garden is bigger and by how much?

# Shelly's garden  area
length = 22
breadth = 15

Area_rectangle = length * breadth  #shelly's garden 

print(f"Shelly's garden area ={Area_rectangle}")

# Rachel's garden area

side = 21

Area_square = side * side # rachel's garden
print(f"Rachel's garden area = {Area_square}")

differnce = abs(Area_rectangle-Area_square)      

if Area_rectangle>Area_square:
    print(f"Shelly's garden is {differnce}m bigger than Rachel's garden")

else:
    print(f"Rachel's garden is {differnce}m bigger than shelly's garden")

