#    1
#   12
#  123
# 1234
#  123
#   12
#    1
for i in range(1, 5):
    for space in range(4-i):
        print(" ", end="")

    for j in range(1, i+1):
        print(j, end="")

    print()

for i in range(3, 0, -1):
    for space in range(4-i):
        print(" ", end="")

    for j in range(1, i+1):
        print(j, end="")

    print()