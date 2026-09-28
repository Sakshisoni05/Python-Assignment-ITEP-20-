# *********
#  ******* 
#   ***** 
#    ***
#     * 

for i in range(5):
    for space in range(i):
        print(" ", end="")

    for star in range(9 - 2*i):
        print("*", end="")

    print()