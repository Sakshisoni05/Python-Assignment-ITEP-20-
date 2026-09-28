#     1
#    212
#   32123
#  4321234
# 543212345

for i in range(1, 6):

    # spaces
    for space in range(5-i):
        print(" ", end="")

    # decreasing numbers
    for j in range(i, 0, -1):
        print(j, end="")

    # increasing numbers
    for j in range(2, i+1):
        print(j, end="")

    print()