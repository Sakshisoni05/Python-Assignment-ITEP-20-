#    *
#   ***
#  ***** 
# ******* 
#  ***** 
#   *** 
#    *

for i in range(1, 5):
    for space in range(4-i):
        print(" ", end="")

    for star in range(2*i-1):
        print("*", end="")

    print()

for i in range(3, 0, -1):
    for space in range(4-i):
        print(" ", end="")

    for star in range(2*i-1):
        print("*", end="")

    print()