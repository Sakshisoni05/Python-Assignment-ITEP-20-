for i in range(7):
    for j in range(7):
        if j == 0 or j == 6:
            print("*", end="")
        elif i >= 4 and (j == i - 3 or j == 10 - i):
            print("*", end="")
        else:
            print(" ", end="")
    print()