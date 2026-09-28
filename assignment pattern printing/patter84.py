#    *
#   *_* 
#  *___* 
# *_____*
#  *___* 
#   *_*
#    *

for i in range(1, 5):
    for space in range(4 - i):
        print(" ", end="")

    print("*", end="")

    for j in range(2 * i - 3):
        print("_", end="")

    if i > 1:
        print("*", end="")

    print()

for i in range(3, 0, -1):
    for space in range(4 - i):
        print(" ", end="")

    print("*", end="")

    for j in range(2 * i - 3):
        print("_", end="")

    if i > 1:
        print("*", end="")

    print()