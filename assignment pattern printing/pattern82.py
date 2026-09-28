# 1
# 1 2
# 1  3
# 1   4
# 1  3
# 1 2
# 1

for i in range(1, 5):
    print(1, end="")

    if i > 1:
        for space in range(2*i - 3):
            print(" ", end="")
        print(i, end="")

    print()

for i in range(3, 0, -1):
    print(1, end="")

    if i > 1:
        for space in range(2*i - 3):
            print(" ", end="")
        print(i, end="")

    print()