# 1
# 12
# 1 3
# 1  4
# 12345
for i in range(1, 6):
    if i == 5:
        for j in range(1, 6):
            print(j, end="")
    else:
        for j in range(1, i + 1):
            if j == 1 or j == i:
                print(j, end="")
            else:
                print(" ", end="")
    print()

    