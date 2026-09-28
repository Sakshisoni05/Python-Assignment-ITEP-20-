for i in range(7):
    for j in range(7):
        if i < 4 and (j == i or j == 6 - i):
            print("*", end="")
        elif i >= 3 and j == 3:
            print("*", end="")
        else:
            print(" ", end="")
    print()