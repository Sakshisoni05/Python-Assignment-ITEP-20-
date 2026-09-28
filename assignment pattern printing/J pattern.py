for i in range(7):
    for j in range(5):
        if i == 0 or j == 4 or (i == 6 and j < 4) or (i == 5 and j == 0):
            print("*", end="")
        else:
            print(" ", end="")
    print()