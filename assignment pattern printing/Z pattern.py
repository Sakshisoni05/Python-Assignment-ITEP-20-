for i in range(7):
    for j in range(7):
        if i == 0 or i == 6 or j == 6 - i:
            print("*", end="")
        else:
            print(" ", end="")
    print()