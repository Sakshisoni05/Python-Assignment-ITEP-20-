#     X 
#    X X 
#   X__X
#  X____X
# X X X X X

for i in range(1, 6):

    for space in range(5, i, -1):
        print(" ", end="")

    for j in range(1, i + 1):

        if i == 1:
            print("X", end=" ")

        elif i == 2:
            print("X", end=" ")

        elif i == 3 and j == 2:
            print("__", end="")

        elif i == 4 and j > 1 and j < 4:
            print("__", end="")

        else:
            print("X", end=" ")

    print()