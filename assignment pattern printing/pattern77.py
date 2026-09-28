# 23456789
# 1     7
# 1   5
# 1 3
# 1

print("23456789")

for i in range(7, 0, -2):
    print("1", end="")

    for space in range(i-1):
        print(" ", end="")

    if i != 1:
        print(i, end="")

    print()