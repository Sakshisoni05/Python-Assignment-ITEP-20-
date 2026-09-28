#     A
#    B B
#   C  C
#  D    D
# EEEEEEEEE

for i in range(1, 6):

    for space in range(5, i, -1):
        print(" ", end="")

    if i == 1:
        print("A")

    elif i == 5:
        print("EEEEEEEEE")

    else:
        print(chr(64 + i), end="")

        for j in range(1, 2 * i - 2):
            print(" ", end="")

        print(chr(64 + i))
        