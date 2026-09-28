# *     *
# **    **
# ***   ***
# ****  ****
# ***** *****

for i in range(1, 6):

    # left stars
    for j in range(i):
        print("*", end="")

    # spaces
    for space in range(6-i):
        print(" ", end="")

    # right stars
    for j in range(i):
        print("*", end="")

    print()